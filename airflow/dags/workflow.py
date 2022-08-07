from airflow import DAG
from datetime import datetime,timedelta
from airflow.models import Connection
from airflow import models, settings
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
import sys
import os
import pandas as pd
import json
 
def set_connection(**config):
    for k,v in config.items():
        conn = Connection()
        setattr(conn, k, v)
        session = settings.Session()
        session.add(conn)
        session.commit()
        session.close()
    
default_args = {"owner":"airflow","start_date":datetime(2021,3,7)}
with DAG(dag_id="workflow",template_searchpath='includes/sql/',default_args=default_args,schedule_interval='@daily', catchup=False) as dag:
    
    task = PythonOperator(
                    dag = dag,
                    task_id = 'set-connections',
                    python_callable = set_connection
                ),
    run_ingestion= PostgresOperator(
                    task_id="run_ingestion",
                    postgres_conn_id="1data_lake",
                    sql="ingestion.sql",
                )

task >> run_ingestion