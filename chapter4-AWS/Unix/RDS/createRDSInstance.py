#!/usr/bin/env python

import boto3
rds = boto3.client('rds')
try:
        response = rds.create_db_instance(
        DBInstanceIdentifier='packtpub-RDS',
        MasterUsername='dbadmin',
        MasterUserPassword='password',
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        AllocatedStorage=5)
        print response
except Exception as error:
        print error
