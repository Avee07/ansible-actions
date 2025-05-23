import boto3
from botocore.client import Config
import os

# --- Environment variables or hardcoded values ---
endpoint_url = os.getenv("S3_ENDPOINT", "http://localhost:9000")
access_key = os.getenv("S3_ACCESS_KEY", "minioadmin")
secret_key = os.getenv("S3_SECRET_KEY", "minioadmin123")
bucket_name = os.getenv("S3_BUCKET", "object-storage")

# --- Step 1: Create dictionary and write to file ---
data = {
    "framework": "GitHub Actions",
    "language": "Python",
    "file": "hello.txt",
    "status": "Success",
    "message": "Hello from GitHub Actions!"
}

with open("hello.txt", "w") as f:
    for key, value in data.items():
        f.write(f"{key}: {value}\n")

# --- Step 2: Create S3 client and upload file ---
s3 = boto3.resource(
    "s3",
    endpoint_url=endpoint_url,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1"
)

s3.Bucket(bucket_name).upload_file("hello.txt", "hello.txt")
print(f"✅ Uploaded 'hello.txt' to bucket '{bucket_name}'")

# --- Step 3: List all files in the bucket ---
print("\n📂 Files in bucket:")
for obj in s3.Bucket(bucket_name).objects.all():
    print(f"- {obj.key}")
