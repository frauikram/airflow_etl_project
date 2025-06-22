from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def process_orders():
    df = pd.read_csv('/opt/airflow/dags/orders.csv')
    df_summary = df.groupby('customer_id')['amount'].sum().reset_index()
    df_summary = df_summary.sort_values(by='amount', ascending=False)
    df_summary.to_csv('/opt/airflow/dags/top_users.csv', index=False)

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='etl_top_users',
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
    description='Simple ETL DAG to process orders and find top users',
    tags=['etl', 'csv'],
) as dag:

    run_etl = PythonOperator(
        task_id='process_orders',
        python_callable=process_orders,
    )

    run_etl
