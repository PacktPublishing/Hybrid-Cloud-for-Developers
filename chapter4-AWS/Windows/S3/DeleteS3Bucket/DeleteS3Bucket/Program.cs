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
            DeleteFilesInS3Bucket(); // invoke the method to list S3 buckets

            Console.ReadKey();
        }
        static void DeleteFilesInS3Bucket()
        {
            try
            {
                IAmazonS3 s3Client = new AmazonS3Client();
                DeleteObjectRequest request = new DeleteObjectRequest()
                {
                    BucketName = "packt-pub",
                    Key = "myfile"
                };

                s3Client.DeleteObject(request);
            }
            catch (AmazonS3Exception s3Exception)
            {
                Console.WriteLine("Error!!");
                Console.WriteLine(s3Exception.ErrorCode);
            }
        }
    }
}