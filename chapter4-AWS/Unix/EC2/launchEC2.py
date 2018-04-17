import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-1853ac65',
    MinCount=1,
    MaxCount=1,
    KeyName="access",
    InstanceType='t1.micro')
print instance[0].id
