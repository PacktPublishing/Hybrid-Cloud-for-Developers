using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Amazon;
using Amazon.RDS;
using Amazon.RDS.Model;
using Amazon.Runtime;
using System.Collections.Specialized;
using System.Configuration;

namespace pactpubAWS
{
    class RDSDemo
    {
        static IAmazonRDS client;
        static void Main(string[] args)
        {
            try
            {
                //create RDS instance
                client = new AmazonRDSClient();
                CreateDBInstanceRequest request = new CreateDBInstanceRequest("packtpubRDS", 5, "db.m1.small", "mysql", "dbadmin", "password");
                client.CreateDBInstance(request);

                // list RDS instances
                DescribeDBInstancesRequest request2 = new DescribeDBInstancesRequest();
                DescribeDBInstancesResponse response2 = new DescribeDBInstancesResponse();
                response2 = client.DescribeDBInstances(request2);
                foreach (DBInstance entry in response2.DBInstances)
                {
                    Console.WriteLine(entry.DBInstanceIdentifier);
                }

                Console.WriteLine("Waiting for 60 seconds before deleting the RDS instance");
                System.Threading.Thread.Sleep(50000);

                // delete RDS instance
                DeleteDBInstanceRequest delete_request = new DeleteDBInstanceRequest("packtpubRDS");
                delete_request.SkipFinalSnapshot = true;
                client.DeleteDBInstance(delete_request);
            }
            catch (AmazonRDSException exception)
            {
                Console.WriteLine("Error!");
                Console.WriteLine(exception.ErrorCode);
                Console.ReadKey();
            }

        }
    }
}