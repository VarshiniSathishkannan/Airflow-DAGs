from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'retries':1,
    'retry_delay':timedelta(minutes=5),
    'email_on_failure':True,
    'email_on_retry':True,
    'email':'kasturig1947@gmail.com'
}

def data_download(**kwargs):
    print("The File is downloaded")
    print(kwargs)
    print(kwargs['ds'])
    return 40 # will be stored in admin page - metadata

def data_write():
    with open('C:/Users/varsh/Airflow/Airflow-DAGs/myfile.txt','w') as f:
        f.write('data')

def failure(context):
    print('The Task failed from callback')
    print(context)

with DAG(dag_id='dag-1',default_args=default_args,schedule_interval='*/30 * * * *',start_date=datetime(2023,7,18), catchup=False, max_active_runs=1) as dag:
    task_1 = DummyOperator(
        task_id='task_1',
        retries=5,
        retry_delay=timedelta(minutes=10)
    )
    task_2 = PythonOperator(
        task_id='Download_data',
        python_callable=data_download
    )
    task_3 = PythonOperator(
        task_id='writing_data',
        python_callable=data_write
    )
    task_4 = FileSensor(
        task_id='waiting_for_data',
        fs_conn_id='fs_default',
        filepath='myfile.txt',
        poke_interval=10
    )
    task_5 = BashOperator(
        task_id='processing_data',
        bash_command='exit 1',
        on_failure_callback=failure
    )

    task_1.set_downstream(task_2)
    task_2.set_downstream(task_3)
    task_3.set_downstream(task_4)
    task_4.set_downstream(task_5)
    task_4.set_upstream(task_1)

    # task_1 >> task_2 << task_3 
    # task_2 >> [task_4, task_5]
    # Cannot create dependency with list on list 
    # we have to use cross dependency in such cases
