using System;
using System.Collections.Generic;
using System.Threading;

using Amazon;
using Amazon.EC2;
using Amazon.EC2.Model;
using Amazon.EC2.Util;

namespace EC2
{
    class EC2Operations
    {
        public static void Main()
        {
            EC2_instance_operations();
        }

        static void EC2_instance_operations()
        {
            try
            {
                // Launch the instance
                AmazonEC2Client ec2 = new AmazonEC2Client();
                RunInstancesRequest request = new RunInstancesRequest();
                request.ImageId = "ami-bf4193c7";  /* AMI ID in your region */
                request.InstanceType = "t1.micro";   /* Flavor */
                request.MinCount = 1;
                request.MaxCount = 1;
                request.KeyName = "access";  /* Name of the key-pair */
                RunInstancesResponse response = ec2.RunInstances(request);

                Console.WriteLine("Launching instance....waiting for 30 seconds..");

                System.Threading.Thread.Sleep(30000);


                // Check the state
                var instances = response.Reservation.Instances;
                var id = instances[0].InstanceId;
                var state = instances[0].State;
                Console.WriteLine("State is : {0}", state.Name);

                Console.WriteLine("Terminating the instance..");

                // Terminate the instance
                var terminate_request = new TerminateInstancesRequest();
                terminate_request.InstanceIds.Add(instances[0].InstanceId);

                var terminate_response = ec2.TerminateInstances(terminate_request);
                var terminating_instance = terminate_response.TerminatingInstances[0];

                Console.WriteLine("Terminating instance : {0}", terminating_instance.InstanceId);
                Console.WriteLine("Instance state : {0}", terminating_instance.CurrentState.Name);
            }
            catch (AmazonEC2Exception exception)
            {
                Console.WriteLine("Error!");
                Console.WriteLine(exception.ErrorCode);
            }
            Console.ReadKey();
        }
    }
}
