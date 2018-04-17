using System;
using Amazon;
using Amazon.SQS;
using Amazon.SQS.Model;

namespace packtpubSQS
{
    class packtpubSQSDemo
    {
        public static void Main(string[] args)
        {
            var sqs_object = new AmazonSQSClient();

            try
            {
                // Create the SQS queue request and give it a name
                var create_queue_request = new CreateQueueRequest
                {
                    QueueName = "packtpub_queue"
                };
                // create the queue and fetch the response object
                var create_queue_response = sqs_object.CreateQueue(create_queue_request);
                string queue_url = create_queue_response.QueueUrl;



                // List queues
                var listQueuesRequest = new ListQueuesRequest();
                var listQueuesResponse = sqs_object.ListQueues(listQueuesRequest);

                if (listQueuesResponse.QueueUrls != null)
                {
                    foreach (String urls in listQueuesResponse.QueueUrls)
                    {
                        Console.WriteLine(" Queue URL : {0}", urls);
                    }
                }

                //Send a message
                Console.WriteLine("Sending a message to MyQueue.\n");
                var send_message_request = new SendMessageRequest
                {
                    QueueUrl = queue_url, //URL from initial queue creation
                    MessageBody = "Welcome, hybrid cloud developers !"
                };
                sqs_object.SendMessage(send_message_request);

                // Recieve a message
                var receive_message_request = new ReceiveMessageRequest { QueueUrl = queue_url };
                var received_message_response = sqs_object.ReceiveMessage(receive_message_request);
                if (received_message_response.Messages != null)
                {
                    foreach (var message in received_message_response.Messages)
                    {
                        if (!string.IsNullOrEmpty(message.MessageId))
                        {
                            Console.WriteLine("MessageId : {0}", message.MessageId);
                        }
                        if (!string.IsNullOrEmpty(message.ReceiptHandle))
                        {
                            Console.WriteLine("ReceiptHandle: {0}", message.ReceiptHandle);
                        }
                        if (!string.IsNullOrEmpty(message.MD5OfBody))
                        {
                            Console.WriteLine("MD5OfBody: {0}", message.MD5OfBody);
                        }
                        if (!string.IsNullOrEmpty(message.Body))
                        {
                            Console.WriteLine("Body: {0}", message.Body);
                        }

                        foreach (string key in message.Attributes.Keys)
                        {
                            Console.WriteLine("Attribute");
                            Console.WriteLine("Name: {0}", key);
                            var value = message.Attributes[key];
                            Console.WriteLine("Value: {0}", string.IsNullOrEmpty(value) ? "(no value)" : value);
                        }
                    }
                }

                // Delete message from queue
                //var message_handle = received_message_response.Messages[0].ReceiptHandle;

                //var deleteRequest = new DeleteMessageRequest
                //{
                //    QueueUrl = queue_url,
                //    ReceiptHandle = message_handle
                //};
                //sqs_object.DeleteMessage(deleteRequest);



            }
            catch (AmazonSQSException exception)
            {
                Console.WriteLine("Error !");
                Console.WriteLine(exception.ErrorCode);
            }
        }
    }
}