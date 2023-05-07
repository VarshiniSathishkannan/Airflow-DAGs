# Airflow DAGs
 Airflow DAGs 

Traditional - write a script - cron job to schedule

Disadvantages:

Failures - no retry policy
Monitoring - success or failure status, runtime
Dependencies - Cannot set dependency between the jobs 
Scalability - no centralised scheduler across different cron machines 
Deployment - Deploy new changes constantly 
Process historic data

Apache Airflow

Developed by Airbnb
Open source
Python

Airflow DAG -  workflow consists of tasks

I am using cloud composer - managed airflow 

We have to create an environment or airflow instance

Each environment has a web server for web gui , a database, rest api and CLI

SQL alchemy

Steps to write an airflow DAG

A DAG file, is just a python script .py file which is a configuration file specifying the DAG’s structure as code

There are only 5 steps we need to remember to write an airflow DAG or workflow

Importing modules
Default arguments
Instantiate DAG
Tasks
Setting up dependencies

DAGs do not perform any actual computation, Operators determine what has to be done

Task - once operator is instantiated, it is referred to as a task. An operator describes a single task in the workflow 

Instantiating requires providing a unique task id and DAG container

Operator types:
Sensor
Operators
Transfers


Sensor - it keeps running until a condition is met, waiting for a certain time, external file or upstream data source

HdfsSensor - waits for a file or folder to land in HDFS
NamedHivePartitionSensor - Check whether the most recent partition of a Hive table is available for downstream processing

Operators - triggers a certail action - run a bash command, python function, Hive query

BashOperator, PythonOperator, HiveOperator, BigqueryOperator


Transfer - Move data from one location to another

MySqlToHiveTranfer - moves data from MySql to Hive

There are so many inbuilt operators

All operators inherit from the BaseOperator, We can create as many operators as we want from the BaseOperator

Task Dependencies are set using,

The set_upstream and set_downstream operators 

The bitshift operators <<  and >>

The key concept of Airflow is the execution time, The execution times begins at the DAG’s start date and repeat every schedule interval, Suppose we specify a date one month back as the start date then airflow will start 30 such instances each gets triggered until the current date

Project

Integration of Bigquery with Airflow
Public Dataset from Bigquery

Create a service account in GCP and create a new key

Save the key as json file 

In Airflow UI, Admin - connections - add a new entry 

Give connection ID (name) connection type (platform) and specify the JSON file path or the JSON itself and the scope which is the entire project

Now Airflow can run anything on GCP platform 

We have to use the BigqueryOperator to query a table and save the results in a Dataset in Bigquery

