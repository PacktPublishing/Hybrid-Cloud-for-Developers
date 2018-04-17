using System;

using Amazon;
using Amazon.SimpleNotificationService;
using Amazon.SimpleNotificationService.Model;

namespace packtpubSNSDemo
{
    class SNSDemo
    {
        public static void Main(string[] args)
        {
            var sns_object = new AmazonSimpleNotificationServiceClient();

            string email_id = "manoj.hirway@gmail.com";

            try
            {
                // Create an SNS topic called "PACKT-PUB"
                Console.WriteLine("Creating topic...");
                var Topic_Arn_id = sns_object.CreateTopic(new CreateTopicRequest
                {
                    Name = "PACKT-PUB"
                }).TopicArn;

                // Set attributes for the topic
                sns_object.SetTopicAttributes(new SetTopicAttributesRequest
                {
                    TopicArn = Topic_Arn_id,
                    AttributeName = "DisplayName",
                    AttributeValue = "PACKT-PUB"
                });

                // Add an email subsciption 
                sns_object.Subscribe(new SubscribeRequest
                {
                    TopicArn = Topic_Arn_id,
                    Protocol = "email",
                    Endpoint = email_id
                });

                // Publish a topic
                sns_object.Publish(new PublishRequest
                {
                    Subject = "Test",
                    Message = "Testing testing 1 2 3",
                    TopicArn = Topic_Arn_id
                });

                Console.WriteLine("Waiting 60 seconds before deleting the topic");
                System.Threading.Thread.Sleep(30000);
                //Delete the topic
                sns_object.DeleteTopic(new DeleteTopicRequest
                {
                    TopicArn = Topic_Arn_id
                });

            }
            catch (AmazonSimpleNotificationServiceException exception)
            {
                Console.WriteLine("Error !");
                Console.WriteLine(exception.ErrorCode);
            }
        }
    }
}