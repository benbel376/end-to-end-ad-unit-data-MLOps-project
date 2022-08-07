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
    conn = Connection(
        conn_id="2data_lake",
        conn_type="Postgres",
        host="postgres",
        login="data_lake",
        password="data_lake",
        schema="data_lake",
        port=5432
    )
    conn2 = Connection(
        conn_id="3staging",
        conn_type="Postgres",
        host="postgres",
        login="staging",
        password="staging",
        schema="staging",
        port=5432
    )
    session = settings.Session()
    session.add(conn)
    session.add(conn2)
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
                    postgres_conn_id="2data_lake",
                    sql="ingestion.sql",
                )
    run_extraction= PostgresOperator(
                    task_id="run_extraction",
                    postgres_conn_id="3staging",
                    sql="extract.sql",
                )

task >> run_ingestion >> run_extraction