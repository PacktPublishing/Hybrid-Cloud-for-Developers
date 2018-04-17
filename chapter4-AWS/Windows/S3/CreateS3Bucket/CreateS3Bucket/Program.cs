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
            createS3Bucket(); // invoke the method to create an S3 bucket

            Console.ReadKey();
        }

        static void createS3Bucket()
        {
            try
            {
                IAmazonS3 s3Client = new AmazonS3Client();
                PutBucketRequest bucket_request = new PutBucketRequest();
                bucket_request.BucketName = "packt-pub";
                s3Client.PutBucket(bucket_request);
            }
            catch (AmazonS3Exception s3exception)
            {
                Console.WriteLine("Error!!");
                Console.WriteLine(s3exception.ErrorCode);
            }

        }
    }
}