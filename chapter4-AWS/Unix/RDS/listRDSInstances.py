#!/usr/bin/env python

import boto3

rds = boto3.client('rds')

try:
        # Fetch the list of all database instances
        dbs = rds.describe_db_instances()

        for db in dbs['DBInstances']:
                print ("MasterUser : %s Endpoint : %s:%s Status:%s") % (
                db['MasterUsername'],
                db['Endpoint']['Address'],
                db['Endpoint']['Port'],
                db['DBInstanceStatus'])
except Exception as error:
                print error
