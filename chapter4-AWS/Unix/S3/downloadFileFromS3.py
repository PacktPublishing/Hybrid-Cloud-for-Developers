import boto3

s3 = boto3.resource('s3')
s3.Bucket('packt-pub-bucket').download_file('test.txt', '/tmp/hello.txt')
