using System;
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
            uploadfile(); // invoke the method to list S3 buckets

            Console.ReadKey();
        }
        static void uploadfile()
        {
            try
            {
                IAmazonS3 s3Client = new AmazonS3Client();
                PutObjectRequest request_obj = new PutObjectRequest()
                {
                    BucketName = "packt-pub",
                    Key = "myfile",
                    FilePath = "D:\\test.txt",
                };
                // Add some metadata to the object to be uploaded and send the PUT request
                request_obj.Metadata.Add("title", "This is the first uploaded file");
                s3Client.PutObject(request_obj);
            }
            catch (AmazonS3Exception s3Exception)
            {
                Console.WriteLine("Error !!");
                Console.WriteLine(s3Exception.ErrorCode);
            }
        }
    }
}