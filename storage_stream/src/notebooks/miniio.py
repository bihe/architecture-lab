import boto3

s3_client = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="password"
)

# Create a bucket
s3_client.create_bucket(Bucket="test-bucket")

# Upload a file
s3_client.put_object(Bucket="test-bucket", Key="example.txt", Body="Hello, MinIO!")