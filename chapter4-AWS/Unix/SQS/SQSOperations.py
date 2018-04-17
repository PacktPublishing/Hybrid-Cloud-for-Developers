import boto3
import time

# Create SQS client
sqs_object = boto3.client('sqs')

response = sqs_object.create_queue(
    QueueName='packtpub_queue',
)

queue_url = response['QueueUrl']

print "Creating queue..."
time.sleep(10)
# Send message to SQS queue
print "Sending message..."
response = sqs_object.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'Hybrid Cloud for Developers'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Manoj Hirway'
        },
        'Publisher': {
            'DataType': 'String',
            'StringValue': 'Packt Publication'
        }
    },
    MessageBody=(
        'Welcome, hybrid cloud developers '
    )
)

print "Recieving message..."
time.sleep(10)
# Recieve message from SQS queue
response = sqs_object.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

print "Response:"
print "------------"
print response
print "Message :"
print "------------"
message = response['Messages']
print message

# delete message from queue
#response = sqs_object.delete_queue(
#    QueueUrl=queue_url
#)
