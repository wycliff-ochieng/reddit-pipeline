from airflow import DAG
from datetime import datetime
from airflow.operators import PythonOperator
import os
import sys


default_args = {
    "owner":"Wycliff Ochieng",
    "start_date": datetime(year=2025,month=5,day=21)
}

file_postfix = datetime.now().strftime(%Y%m%d)

dag = DAG(
    default_args=default_args,
    catch_up=False,
    interval='@daily',
)


#Extraction from reddit

extract = PythonOperator(
    task_id="extracting",
    python_callable="",
    time_filter="",
    limit=100
)


#uploading to s3