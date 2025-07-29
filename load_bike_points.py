import os
import boto3
from dotenv import load_dotenv

def load_bikes():

    load_dotenv()

    aws_access = os.getenv('ACCESS_KEY')
    aws_secret = os.getenv('SECRET_ACCESS_KEY')
    bucket = os.getenv('AWS_BUCKET_NAME')

    s3_client = boto3.client(
        's3',
        aws_access_key_id = aws_access,
        aws_secret_access_key = aws_secret
    )

    try:
        file = os.listdir('data')[0]
        filename = 'data/'+file
        s3file= 'bike-point/'+file
        try:
            s3_client.upload_file(filename,bucket,s3file)
            print('Upload successful')
            os.remove(filename)
        except:
            print('Could not upload')
    except:
        print('No file 😠')
