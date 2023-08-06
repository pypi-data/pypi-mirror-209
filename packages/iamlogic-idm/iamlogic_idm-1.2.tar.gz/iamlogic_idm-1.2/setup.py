from setuptools import setup, find_packages

setup(
    name='iamlogic_idm',
    version='1.2',
    description='IAMLOGIC IDM package',   
    author_email='info@iamlogic.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'cryptography',
        'sqlalchemy',
        'mysql-connector-python',
        'hvac'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

