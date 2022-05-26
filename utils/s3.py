import boto3
import botocore 
import os
from botocore.exceptions import ClientError
from botocore.config import InvalidRetryConfigurationError
from flask_restful import Resource, reqparse



def push_to_s3(file_name, bucket_name, object_name=None): 


	if object_name is None: 
		object_name = os.path.basename(file_name)

	s3_client = boto3.client('s3')

	try: 
		response = s3_client.upload_file(file_name, bucket_name, object_name)
	except ClientError as error:
		return error

	s3_config = Config(signature_version=botocore.UNSIGNED)
	url = boto3.client('s3', config=s3_config).generate_presigned_url(
		'get_object',
		ExpiresIn=0,
		Params={'Bucket': bucket_name, 'Key': object_name})

	return  url
