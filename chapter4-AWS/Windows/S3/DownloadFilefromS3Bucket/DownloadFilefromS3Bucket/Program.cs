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
           downloadfile(); // invoke the method to list S3 buckets

            Console.ReadKey();
        }
        static void downloadfile()
        {
            try
            {
                IAmazonS3 s3Client = new AmazonS3Client();      /* create an S3 client object */
                GetObjectRequest request = new GetObjectRequest()  /* create a request object */
                {
                    BucketName = "packt-pub",                      /* parameters to the constructor */
                    Key = "myfile"
                };

                using (GetObjectResponse response = s3Client.GetObject(request)) /* capture the response*/
                {
                    string title = response.Metadata["x-amz-meta-title"];
                    Console.WriteLine("The title of the file is : {0}", title);
                    /* set the location of the destination file */
                    string destination_file = "D:\\download\\downloaded_file";
                    if (!File.Exists(destination_file))
                    {
                        response.WriteResponseStreamToFile(destination_file);   /* write the downloaded file*/
                    }
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