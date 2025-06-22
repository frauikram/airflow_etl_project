
# Apache Airflow ETL Project

This is a beginner-friendly ETL pipeline project using **Apache Airflow** with **Docker Compose**. It reads a CSV file, performs simple transformations using pandas, and writes the output to another CSV file.

## 🛠️ Project Stack

- **Apache Airflow** (via Docker Compose)
- **Python**
- **pandas**
- **Postgres** (as Airflow metadata DB)
- **Redis** (for scheduler/message queue)

## 📁 Project Structure

```
.
├── dags/                  # Airflow DAGs
│   └── etl_csv_pipeline.py
├── data/                  # Input and output CSVs
│   ├── raw/customers.csv
│   └── processed/processed_customers.csv
├── docker-compose.yaml    # Airflow setup
├── .env                   # Airflow environment config
├── logs/                  # Airflow logs
└── plugins/               # (empty, for future custom plugins)
```

## ▶️ How to Run

1. Clone the repo and navigate to the directory:

   ```bash
   git clone https://github.com/yourusername/airflow_etl_project.git
   cd airflow_etl_project
   ```

2. Start the Airflow containers:

   ```bash
   docker compose up airflow-init
   docker compose up
   ```

3. Visit [http://localhost:8080](http://localhost:8080)  
   Login with:
   - **Username**: `airflow`
   - **Password**: `airflow`

4. Trigger the DAG `etl_csv_pipeline` to run the ETL job.

## ✅ Output

After successful DAG execution:
- You’ll find a `processed_customers.csv` file with cleaned and deduplicated customer records in `data/processed`.

## 📄 License

This project is open-source and free to use.
