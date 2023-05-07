import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from datetime import timedelta

default_args = {
    'owner':'Varshini',
    'depends_on_past':False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email':'varshinisathish2112@gmail.com',
    'email_on_failure':True,
    'email_on_retry':True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'Bigquery_Extract',
    default_args=default_args,
    description='Extract Hackers News Full data',
    schedule_interval="0 0 * * *"
)

BQ_CONN_ID = 'my_gcp_conn'
BQ_PROJECT_ID = 'nodal-empire-382814'
BQ_DATASET = 'Hackers_news'

t1 = BigQueryOperator(
    task_id='Extract', #cannot have space 
    dag=dag,
    depends_on_past=False,
    sql="SELECT string_field_0 as country,string_field_1 as abbr2, string_field_2 as abbr3 FROM `{}.{}.country_codes`;".format(BQ_PROJECT_ID,BQ_DATASET),
    use_legacy_sql=False,
    gcp_conn_id=BQ_CONN_ID,
    destination_dataset_table="{}.{}.output".format(BQ_PROJECT_ID,BQ_DATASET)
)

# t2 = BashOperator(
#     task_id='sleep',
#     bash_command='sleep 5',
#     dag=dag,
#     depends_on_past=False
# )

# t1 >> t2