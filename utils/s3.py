import boto3
import botocore
import os
from botocore.exceptions import ClientError
from botocore.config import InvalidRetryConfigurationError
from flask_restful import Resource, reqparse

bucket_name = 'pf-webs-s3'


def push_to_s3(file_name, object_name=None):

    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(
            file_name,
            bucket_name,
            object_name,
            ExtraArgs={'ACL': 'public-read',
                       "ContentType": file_name.content_type}
        )
    except ClientError as e:
        return e

    config = Config(signature_version=botocore.UNSIGNED)
    fotoUrl = boto3.client('s3', config=config) \
        .generate_presigned_url(
            'get_object',
            ExpiresIn=0,
            Params={'Bucket': bucket_name, 'Key': object_name}
    )

    return fotoUrl
