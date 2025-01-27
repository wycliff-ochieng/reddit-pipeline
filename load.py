import boto3
import os
import csv
import pandas as pd
import psycopg2

s3 = boto3.client('s3')
bucket_name = 'reddit-backo'
file_path = r'\Users\Admin\Desktop\data-eng\reddit_data_eng\reddit.csv'
s3_key = 'rawData/reddit.csv'
#s3_key = "reddit-backo/rawData/reddit.csv"

def load_to_bucket(s3_key,file_path,bucket_name):
    try:
        s3.upload_file(file_path,bucket_name,s3_key)
        print("loaded successfully")
    except Exception as e:
        print("Not loaded ")

load_to_bucket(s3_key,file_path,bucket_name)


def load_to_db(table_name):
    conn = psycopg2.connect(
        host = 'localhost',
        port = 5433,
        user = 'postgres',
        password = 'mGFeanZG',
        database = 'postgres'
    )

    cursor = conn.cursor()

    df = pd.read_csv('reddit.csv')

    with open('reddit.csv', 'r',encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        
        for row in csvreader:
            cursor.execute(f"INSERT INTO {table_name}(id,title,url,content,author,full_name,event_time,relative_url,score,upvote_ratio,no_comments,subreddit_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
            
            conn.commit()
            print("Loaded to postgres")
            #conn.close()

table_name = 'reddit_posts'
load_to_db(table_name)
