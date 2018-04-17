#!/usr/bin/env python

import boto3

rds = boto3.client('rds')

try:
    response = rds.delete_db_instance(
        DBInstanceIdentifier="packtpub-rds",
        SkipFinalSnapshot=True)
    print response
except Exception as error:
    print error
