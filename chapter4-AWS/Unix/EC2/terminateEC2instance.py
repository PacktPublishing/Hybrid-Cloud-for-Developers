import boto3

ec2 = boto3.resource('ec2')

instance = ec2.Instance("i-05c20ddae4472f9ec")
response = instance.terminate()
print response 
