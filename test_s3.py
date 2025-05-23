import boto3
from botocore.client import Config
import os

endpoint = os.environ["S3_ENDPOINT"]
access_key = os.environ["S3_ACCESS_KEY"]
secret_key = os.environ["S3_SECRET_KEY"]
bucket_name = os.environ["S3_BUCKET"]

print(f"🔌 Connecting to S3 at {endpoint}")
print("🔑 Access Key: {access_key}")
print("🔑 Secret Key:   {secret_key}"  )
print("🗑️ Bucket: {bucket_name}")

# Connect to MinIO
s3 = boto3.resource(
    's3',
    endpoint_url=endpoint,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

# Upload a file (or create a sample one)
with open("hello.txt", "w") as f:
    f.write("Hello from GitHub Actions!")

s3.Bucket(bucket_name).upload_file("hello.txt", "hello.txt")

print(f"✅ Uploaded 'hello.txt' to bucket '{bucket_name}'")
