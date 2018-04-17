import boto3

with open('bucket.yaml') as template_file:
    template = template_file.read()

cloud_formation_object = boto3.resource('cloudformation')

response = cloud_formation_object.create_stack(StackName = 'packtpubstack',TemplateBody = template)
print(response)
print(type(response))
