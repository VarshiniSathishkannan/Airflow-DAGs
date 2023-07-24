from airflow import DAG
from datetime import datetime, timedelta

dag = DAG(
    dag_id='dag-2',
    description='I created this DAG',
    start_date=datetime(2023,7,23),
    schedule_interval='*/10 * * * *',
    dagrun_timeout=timedelta(minutes=30),
    tags=['Data Science','Customer'],
    catchup=False
)