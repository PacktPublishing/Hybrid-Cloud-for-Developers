import boto3

# Create an SNS client object
sns_client = boto3.client(
    "sns",
   # You may have to set the AWS credentials of you haven't already set using AWS CLI
   # aws_access_key_id="YOUR ACCES KEY",   
   # aws_secret_access_key="YOUR SECRET KEY",
   # region_name=us-east-1
)

# Create an SNS topic
sns_topic = sns_client.create_topic(Name="packt-pub")
topic_arn = sns_topic['TopicArn']        # fetch the resource name

# Add an email address subscription
sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint='manoj.hirway@gmail.com'       # email address of the recipient
)


# Publish a message.
sns_client.publish(Message="Welcome hybrid cloud developers!", TopicArn=topic_arn)

# delete the topic
#response = sns_client.delete_topic(
#    TopicArn=topic_arn
#)
