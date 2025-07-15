import os
import boto3
from dotenv import load_dotenv

load_dotenv()

aws_access = os.getenv('ACCESS_KEY')
aws_secret = os.getenv('SECRET_ACCESS_KEY')
bucket = os.getenv('AWS_BUCKET_NAME')

s3_client = boto3.client(
    's3',
    aws_access_key_id = aws_access,
    aws_secret_access_key = aws_secret
)

filename = 'data/2025-07-15_10-13-29.json'
s3file= 'bike-point/2025-07-15_10-13-29.json'

s3_client.upload_file(filename,bucket,s3file)
