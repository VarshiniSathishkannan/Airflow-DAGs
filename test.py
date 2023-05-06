import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
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
    'Test',
    default_args=default_args,
    description='Testing my new DAG',
    schedule_interval=timedelta(days=1)
)

# priority_weight has type int in Airflow DB, uses the maximum.
t1 = BashOperator(
    task_id='echo',
    bash_command='echo test',
    dag=dag,
    depends_on_past=False
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag,
    depends_on_past=False
)

# t3 = BashOperator(
#     task_id='print date',
#     bash_command='date',
#     dag=dag,
#     depends_on_past=False
# )

t1 >> t2