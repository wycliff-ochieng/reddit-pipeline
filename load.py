import boto3
import os

s3 = boto3.client('s3')
bucket_name = 'reddit-backo'
file_name = 'reddit.csv'
s3_key = f'{file_name}'
#s3_key = "reddit-backo/rawData/reddit.csv"

def load_to_bucket(s3_key,file_name,bucket_name):
    try:
        s3.upload_file(s3_key,file_name,bucket_name)
        print("loaded successfully")
    except Exception as e:
        print("Not loaded ")

load_to_bucket(s3_key,file_name,bucket_name)

