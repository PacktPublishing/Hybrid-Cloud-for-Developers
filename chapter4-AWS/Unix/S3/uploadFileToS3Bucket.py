import boto3

s3 = boto3.resource('s3')

file_handle = open('/home/packt-pub/test.txt', 'r')

s3.Bucket('packt-pub-bucket').put_object(Key='test.txt', Body=file_handle)
