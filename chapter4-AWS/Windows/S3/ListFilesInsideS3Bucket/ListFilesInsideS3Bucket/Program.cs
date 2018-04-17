using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Collections.Specialized;
using System.Configuration;

using Amazon;
using Amazon.S3;
using Amazon.S3.Model;

namespace pactpubAWS
{
    class S3Demo
    {
        public static void Main(string[] args)
        {
            listFilesInS3Bucket(); // invoke the method to list S3 buckets

            Console.ReadKey();
        }
        static void listFilesInS3Bucket()
        {
            try
            {
                IAmazonS3 s3Client = new AmazonS3Client();   /* create an S3 client object */
                ListObjectsRequest list_request = new ListObjectsRequest(); /* create a request object */
                list_request.BucketName = "packt-pub";        /* specify the bucket name in the object */

                ListObjectsResponse list_response = s3Client.ListObjects(list_request);  /* invoke the request */

                foreach (S3Object entry in list_response.S3Objects)     /* iterate through the response list */
                {
                    Console.WriteLine("key = {0} size = {1}", entry.Key, entry.Size);  /* print keys and sizes */
                }
            }
            catch (AmazonS3Exception s3Exception)
            {
                Console.WriteLine("Error!!");
                Console.WriteLine(s3Exception.ErrorCode);
            }
        }
    }
}