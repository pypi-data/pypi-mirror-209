from IDMConnector import ConnectorClass
import time, json, logging, mysql.connector, traceback, ast
from datetime import timedelta

logger = logging.getLogger()

#######################
#  Initialize_IDM_DB  #
#######################
class Initialize_IDM_DB(object):
    # To initiate a database connection
    # Creating a variable to call the connection object
    def __init__(self, db_local):
        logger.debug("--inside:Initialize_IDM_DB() init--")
        self.db_local = db_local
        self.db_conn = None
        self.db_cursor = None

    # This ensure, whenever an object is created using "with"
    # this magic method is called, where you can create the connection.
    def __enter__(self):        
        self.db_conn = mysql.connector.connect(**self.db_local)
        self.db_cursor = self.db_conn.cursor(dictionary=True)
        return self

    # once the with block is over, the __exit__ method would be called
    # with that, you close the connnection
    def __exit__(self, exception_type, exception_val, trace):        
        try:
           logger.debug("---INSIDE __exit__ close the connnection---")
           self.db_cursor.close()
           self.db_conn.close()
        except AttributeError: # isn't closable           
           return True # exception handled successfully
        
    # To perform operations such as create, update, delete etc. 
    # To retrieve all reconcilation data from IDM database.    
    def retrieve_reconciliation_data(self, mappingid, log_level):  
        logger.setLevel(log_level)     
        logger.debug("inside:Initialize_IDM_DB() , reconciliation_for_operation() func:")    
        self.db_cursor.execute("SELECT * FROM reconcile_sync_data WHERE mapping_id=%s"%(mappingid))
        self.result = self.db_cursor.fetchall()
        return self.result
    
    # To update reconciliation statistics whether success of the operation causes a mid-operation error.
    # Passing the statistics message and update the message for each reconcilation operations.
    def update_reconciliation_statistics(self, mappingid, json_data, actions, data):
        logger.debug("inside:Initialize_IDM_DB() , update_reconciliation_statistics() func:")        
        update_query = "UPDATE reconcile_sync_data SET statistics=%s WHERE mapping_id = %s AND reconcile_data = %s AND actions = %s"
        values = (
            data,
            mappingid,
            json_data,
            actions
        )
        self.db_cursor.execute(update_query, values)
        self.db_conn.commit()

    # To update reconciliation role sync statistics whether success of the operation causes a mid-operation error.
    # Passing the role statistics message and update the message for each reconcilation operations.
    def update_reconcile_role_sync_data_statistics(self, mappingid, json_str_data, action, msg_data):
        logger.debug("inside:Initialize_IDM_DB() , update_reconcile_role_sync_data_statistics() func:")
        update_role_query = "UPDATE reconcile_role_sync_data SET role_statistics=%s WHERE mapping_id = %s AND role_reconcile_data = %s AND role_actions = %s"
        value = (
                msg_data,
                mappingid,  
                json_str_data,              
                action
            )
        
        self.db_cursor.execute(update_role_query, value)
        self.db_conn.commit()
    
#######################
#  IDMOperationClass  #
#######################
class IDMOperationClass(object):

    # This initialization is used to create an object for the IDMConnector to call the inside of the class methods.
    def __init__(self, configobject):
        self.idm_operation_obj = ConnectorClass(configobject)
    
    # This method tries several times to get the connection back from the server.
    # 'True' is returned. If connection is back.
    # 'None' is returned. If the connection is not connected after several attempts
    def retry_attempt(self, config_param=None, max_attempt=None, delay=5):
        i = 0
        for attempt in range(1, max_attempt+1):
            i = i+1
            try:
                result = self.idm_operation_obj.testConfig(config_param)
                logger.info(f"retry_attempt() func: try attempt-{i}")
                if(result["status"]):
                    logger.info(f"retry_attempt() func: succeed-{i}")
                    logger.debug(result)
                    self.__init__(config_param)
                    return result["status"]
            except Exception as e:
                if attempt < max_attempt:
                    time.sleep(delay)
                    logger.info(f"retry_attempt() func: exception attempt-{i}")
                    logger.error(str(e))
        return None

    # sync method used to perform create, update, delete, ignore operations.
    # Update success/exception for each reconcilation.
    # When the connection is disconnected from the server side during mid-operation, retry the connection.
    # Calculating the reconcilation time is how long it takes to complete all the tasks.
    # Finally return the reconcilation total duration and sync status.    
    def sync(self, mappingid, config_data, log_level, db_config, secret_key) -> dict:                
        logger.setLevel(log_level)
        logger.debug("inside:ConnectorClass() , sync() func:")
        # Get a secret from vault server           
        db_config["passwd"] = secret_key    
        start_time = time.time()      
        msg = "success"
        current_obj_id = 0        
        # Processed Operation records
        processed_operation = set()
        # DB Sync operation call
        with Initialize_IDM_DB(db_config) as obj:
            response = obj.retrieve_reconciliation_data(mappingid, log_level)
            while current_obj_id < len(response):
                obj = response[current_obj_id]
                logger.debug(f"response obj:{obj['id']}")
                logger.debug(f"Processed Operation:{processed_operation}")
                try:
                    logger.debug(f"obj{obj['id']}_currentObj{current_obj_id}")
                    if(obj['actions'] == "create"):
                        json_create_data = obj['reconcile_data']
                        logger.debug("inside:ConnectorClass() , sync() func if create try:")
                        createOp_response = self.idm_operation_obj.create(json.loads(obj['reconcile_data']))
                        logger.debug(createOp_response)
                        
                        with Initialize_IDM_DB(db_config) as dbObj:
                            dbObj.update_reconciliation_statistics(mappingid, json_create_data, obj['actions'], msg)
                        # Role Operation for User
                        if "user_role_data" in json.loads(obj['reconcile_data']):
                            logger.debug("inside:ConnectorClass() , sync() func if create try: inside role operation create")
                            json_create_load_reconcile_data = json.loads(obj['reconcile_data'])
                            if json_create_load_reconcile_data["role_operation"] == "ADD":
                                logger.debug("inside:ConnectorClass() , sync() func if create try: inside role operation create: ADD")
                                for create_groups in json_create_load_reconcile_data["user_role_data"]["group"]:                                    
                                    json_create_str_reconcile_data = str(json_create_load_reconcile_data["user_role_data"])
                                    # Assign user to role call
                                    self.idm_operation_obj.assignUserToRole(json_create_load_reconcile_data["user_role_data"]["username"], create_groups)
                                    # Role Statistics Update
                                    with Initialize_IDM_DB(db_config) as grpObj:
                                        grpObj.update_reconcile_role_sync_data_statistics(mappingid, json_create_str_reconcile_data, "ADD", "role_added_to_user_success")

                    elif(obj['actions'] == "update"):
                        json_update_data = obj['reconcile_data']
                        logger.debug("inside:ConnectorClass() , sync() func elif update try:")
                        updateOp_response = self.idm_operation_obj.update(json.loads(obj['reconcile_data']))
                        with Initialize_IDM_DB(db_config) as dbObj:
                            dbObj.update_reconciliation_statistics(mappingid, json_update_data, obj['actions'], msg)
                        # Role Operation for User
                        if "user_role_data" in json.loads(obj['reconcile_data']):
                            logger.debug("inside:ConnectorClass() , sync() func elif update try: inside role operation update")
                            json_load_reconcile_data = json.loads(obj['reconcile_data'])
                            if json_load_reconcile_data["role_operation"] == "ADD":
                                logger.debug("inside:ConnectorClass() , sync() func elif update try: inside role operation update: ADD")
                                for add_groups in json_load_reconcile_data["user_role_data"]["group"]:
                                    # logger.debug(json_load_reconcile_data["user_role_data"]["username"])
                                    # logger.debug(add_groups)
                                    json_str_reconcile_data = str(json_load_reconcile_data["user_role_data"])
                                    # Assign user to role call
                                    self.idm_operation_obj.assignUserToRole(json_load_reconcile_data["user_role_data"]["username"], add_groups)
                                    # Role Statistics Update
                                    with Initialize_IDM_DB(db_config) as grpObj:
                                        grpObj.update_reconcile_role_sync_data_statistics(mappingid, json_str_reconcile_data, "ADD", "role_added_to_user_success")

                            elif json_load_reconcile_data["role_operation"] == "REMOVE":
                                logger.debug("inside:ConnectorClass() , sync() func elif update try: inside role operation update: REMOVE")
                                for rem_groups in json_load_reconcile_data["user_role_data"]["group"]:
                                    logger.debug(json_load_reconcile_data["user_role_data"]["username"])
                                    logger.debug(rem_groups)
                                    json_str_reconcile_data = str(json_load_reconcile_data["user_role_data"])
                                    # Remove user to role call
                                    self.idm_operation_obj.RemoveUserToRole(json_load_reconcile_data["user_role_data"]["username"], rem_groups)
                                    # Role Statistics Update
                                    with Initialize_IDM_DB(db_config) as grpObj:
                                        grpObj.update_reconcile_role_sync_data_statistics(mappingid, json_str_reconcile_data, "REMOVE", "role_removed_to_user_success")
                                        
                    elif(obj['actions'] == "delete"):
                        json_delete_data = obj['reconcile_data']
                        logger.debug("inside:ConnectorClass() , sync() func elif delete try:")
                        deleteOp_response = self.idm_operation_obj.delete(json.loads(obj['reconcile_data']))
                        with Initialize_IDM_DB(db_config) as dbObj:
                            dbObj.update_reconciliation_statistics(mappingid, json_delete_data, obj['actions'], msg)
                        # Role Operation for User
                        if "user_role_data" in json.loads(obj['reconcile_data']):
                            logger.debug("inside:ConnectorClass() , sync() func elif delete try: inside role operation delete")
                            json_delete_load_reconcile_data = json.loads(obj['reconcile_data'])
                            if json_delete_load_reconcile_data["role_operation"] == "REMOVE":
                                logger.debug("inside:ConnectorClass() , sync() func elif delete try: inside role operation delete: REMOVE")
                                for remove_groups in json_delete_load_reconcile_data["user_role_data"]["group"]:                                    
                                    json_del_str_reconcile_data = str(json_delete_load_reconcile_data["user_role_data"])
                                    # Assign user to role call
                                    self.idm_operation_obj.assignUserToRole(json_delete_load_reconcile_data["user_role_data"]["username"], remove_groups)
                                    # Role Statistics Update
                                    with Initialize_IDM_DB(db_config) as grpObj:
                                        grpObj.update_reconcile_role_sync_data_statistics(mappingid, json_del_str_reconcile_data, "REMOVE", "role_removed_to_user_success")

                    elif(obj['actions'] == "ignore"):
                        json_ignore_data = obj['reconcile_data']
                        logger.debug("inside:ConnectorClass() , sync() func elif ignore try:")
                        ignore_msg = "No operation can be performed which is ignored by behaviour" 
                        with Initialize_IDM_DB(db_config) as dbObj:
                            dbObj.update_reconciliation_statistics(mappingid, json_ignore_data, obj['actions'], ignore_msg)
                    processed_operation.add(obj['id'])
                    current_obj_id += 1
                except Exception as e:
                    logger.debug("inside:ConnectorClass() , sync() except Exception:")
                    _exception = traceback.format_exc()
                    logger.warning(_exception)
                    with Initialize_IDM_DB(db_config) as dbObj:
                        dbObj.update_reconciliation_statistics(mappingid, obj['reconcile_data'], obj['actions'], _exception)
                    try:
                        # Check the connection if any exception occurs
                        conn_test_res = self.idm_operation_obj.testConfig(config_data)
                        if conn_test_res["status"]:
                            logger.debug(f"connection is available,try response_obj_operation:{obj['id']}")
                            self.idm_operation_obj.__init__(config_data)
                            current_obj_id += 1
                    except Exception as e:
                        # if testConfig() is false try again                        
                        logger.info(f"Re-attempt before check, response_obj_operation:{obj['id']}")
                        conn_attempt_resp = self.retry_attempt(config_param=config_data, max_attempt=int(config_data['retry']))
                        if(conn_attempt_resp and conn_attempt_resp is not None):
                            logger.info(f"Re-attempt if conn true, response_obj_operation:{obj['id']}")
                            current_obj_id -= 1
                        else:
                            logger.info(f"Many re-attempt connectivity failed, response_obj_operation:{obj['id']}")
                            return {"error": "Please check the target application server connectivity. Many attempt could not connected!."}

        end_time = time.time()
        duration = end_time - start_time
        duration_str = str(timedelta(seconds=duration))
        return {"total_duration":duration_str, "status": "Reconcilation Sync Completed!"}