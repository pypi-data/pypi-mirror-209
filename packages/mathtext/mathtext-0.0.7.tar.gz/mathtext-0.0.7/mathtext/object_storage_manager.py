"""  This file is run when the model is created in multilabel_intent_recognition.py.  

It automatically uploads as public files the most recent model and dataset to an object storage service (Digital Ocean Spaces).
"""

import os
import re
from datetime import datetime
import boto3
import botocore
import mimetypes

from mathtext.constants import OBJECT_STORAGE_ENDPOINT_URL, OBJECT_STORAGE_REGION_NAME, OBJECT_STORAGE_AWS_ACCESS_KEY_ID, OBJECT_STORAGE_AWS_SECRET_ACCESS_KEY, OBJECT_STORAGE_NAME


def set_client_session():
    session = boto3.session.Session()

    # Create a connection to the Space
    client = session.client(
        's3',
        endpoint_url=OBJECT_STORAGE_ENDPOINT_URL,
        # config=botocore.config.Config(s3={'addressing_style': 'virtual'}),
        region_name=OBJECT_STORAGE_REGION_NAME,
        aws_access_key_id=OBJECT_STORAGE_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=OBJECT_STORAGE_AWS_SECRET_ACCESS_KEY
    )
    return client
    # Tell the space name


def get_object_store_buckets(client, bucket_name):
    try:
        response = client.list_objects_v2(Bucket=bucket_name)
    except:
        print(f"Bucket '{bucket_name}' does not exist.")

    # Filter through response object for folder names
    objs = [obj['Key'] for obj in response['Contents']]
    return objs


def find_current_max_version(buckets):
    current_version = -1

    for obj in buckets:
        try:
            result = re.search(r'v(\d+)', obj)
            match = int(result.group(1))
        except:
            continue

        if match > current_version:
            current_version = match
    next_version = current_version + 1

    return current_version, next_version


def upload_file(client, file_path, bucket_name, spaces_path):
    client.upload_file(
        file_path,
        bucket_name,
        spaces_path,
        ExtraArgs={'ACL': 'public-read'}
    )


def upload_to_object_storage(csv_path, model_path):
    client = set_client_session()
    bucket_name = OBJECT_STORAGE_NAME

    buckets = get_object_store_buckets(client, bucket_name)

    current_version, next_version = find_current_max_version(buckets)

    current_date = datetime.now().strftime('%Y%m%d')

    dataset_file_name = f'rori_multilabeled_data_{current_date}.csv'
    model_file_name = f'multi_intent_recognizer_{current_date}.pkl'

    client.upload_fileobj(
        csv_path,
        bucket_name,
        f'v{next_version}/{dataset_file_name}',
        ExtraArgs={'ACL': 'public-read'}
    )

    upload_file(
        client,
        str(model_path),
        bucket_name,
        f'v{next_version}/{model_file_name}'
    )

    print(f"""
    Upload to Object Storage Successful!

    Remember to update the .env variables with the most current model in the production and staging servers.

    CURRENT_MODEL_LINK='v{next_version}/{model_file_name}'
    CURRENT_MODEL_FILENAME='{model_file_name}'
    """)
    return {
        'model_version': next_version,
        'model': model_file_name,
        'dataset': dataset_file_name
    }
