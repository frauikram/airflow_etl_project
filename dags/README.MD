Apache Airflow CSV ETL Project
A minimal ETL pipeline using Apache Airflow to extract data from a CSV, transform it, and load the top customers back into a CSV. Ideal for portfolio demos.

📁 Structure
bash
Copy
Edit
.
├── dags/
│   ├── etl_pipeline.py
│   └── orders.csv
├── logs/
├── plugins/
├── .env
├── docker-compose.yaml
🔧 Setup
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/airflow_etl_project
cd airflow_etl_project
docker compose up airflow-init
docker compose up
Access at: http://localhost:8080
Login: airflow / airflow

🧠 DAG Tasks
extract(): Read from CSV

transform(): Aggregate totals

load(): Save top_users.csv

📦 Output
See dags/top_users.csv after a run.