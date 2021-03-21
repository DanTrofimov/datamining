import os
import datetime as dt

import requests
import pandas as pd
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

from main import worker

args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 2, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(dag_id='vk_parser_dagger', default_args=args, schedule_interval=None) as dag:
    parse_vk_wall = PythonOperator(
        task_id='vk_parsing',
        python_callable=worker,
        dag=dag
    )
