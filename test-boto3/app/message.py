import boto3
import os

bucket_name = os.getenv('BUCKET_NAME', None)

s3_client = boto3.client('s3')

with open("./books_gr.csv", "rb") as f:
    s3_client.upload_fileobj(f, bucket_name, "books_gr.csv")
