import boto3
from botocore.exceptions import NoCredentialsError
from ..config import settings

def upload_document_to_s3(file, file_name):
    s3 = boto3.client('s3', aws_access_key_id='your_aws_key', aws_secret_access_key='your_aws_secret')
    try:
        s3.upload_fileobj(file, 'your_bucket_name', file_name)
        return f"https://your_bucket_name.s3.amazonaws.com/{file_name}"
    except NoCredentialsError:
        return "Credentials not available"
