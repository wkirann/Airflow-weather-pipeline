# Weather Data Pipeline with Apache Airflow

## Overview
This project demonstrates a full **ETL pipeline** using **Apache Airflow**, **Postgres**, and **Docker**.  
It fetches **real-time weather data** for Nashik, India, stores it in Postgres, and optionally exports it to CSV for analysis or visualization.

## Features
- Fetches weather data from an API
- Stores data in Postgres
- Export data to CSV for reporting
- Fully automated scheduling with Airflow DAG
- Containerized using Docker for easy deployment

## Tech Stack
- **Apache Airflow**: Orchestration
- **Postgres**: Database
- **Docker & Docker Compose**: Containerization
- **Python**: ETL logic (requests, pandas)

## Project Structure
``` 
 airflow-weather-pipeline/
├── dags/
│ └── weather_pipeline_nashik.py
├── docker-compose.yaml
├── .env
├── requirements.txt
├── README.md
└── .gitignore

```

  
## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/airflow-weather-pipeline.git
cd airflow-weather-pipeline 

# 2.Create a .env file in the project root:
```
AIRFLOW_UID=50000
AIRFLOW__WEBSERVER__DEFAULT_USER=airflow
AIRFLOW__WEBSERVER__DEFAULT_PASSWORD=airflow
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow
```
# 3.Install Dependencies
pip install -r requirements.txt

# 4. Start Docker Containers
docker compose up -d

# 5. Access Airflow UI
- Open your browser: http://localhost:8080
- Login with credentials from .env
- Trigger DAG manually or let it run on schedule

# 6. Verify Data
- Open Postgres (e.g., DBeaver) → check table weather_data








