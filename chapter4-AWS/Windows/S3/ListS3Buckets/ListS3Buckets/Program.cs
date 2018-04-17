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
            listS3Buckets(); // invoke the method to list S3 buckets

            Console.ReadKey();
        }
        static void listS3Buckets()
        {
            try
            {
                IAmazonS3 s3Client = new AmazonS3Client();
                ListBucketsResponse list_bucket_response = s3Client.ListBuckets();
                foreach (S3Bucket bucket_object in list_bucket_response.Buckets)
                {
                    Console.WriteLine("Bucket Name: {0}", bucket_object.BucketName);
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