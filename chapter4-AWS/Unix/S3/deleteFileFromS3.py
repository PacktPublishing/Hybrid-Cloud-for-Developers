import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('packt-pub-bucket')
bucket.delete_objects( Delete = {'Objects': [
            {
                'Key': 'test.txt',
            },
        ],
        'Quiet': True
    })
