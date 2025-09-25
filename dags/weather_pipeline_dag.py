from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import requests
import os

# Read API key from environment
API_KEY = os.getenv("3929629872df83fb78cdaa7b06469f0f")
CITY = "Nashik,IN"

def fetch_weather():
    # Fetch weather from OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Nashik,IN&appid=3929629872df83fb78cdaa7b06469f0f&units=metric"
    response = requests.get(url)
    data = response.json()
    
    # Extract useful fields
    weather_data = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }

    # Connect to Postgres using PostgresHook
    pg_hook = PostgresHook(postgres_conn_id="my_postgres")
    conn = pg_hook.get_conn()
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temp REAL,
            humidity INT,
            description TEXT,
            dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert weather data
    cur.execute("""
        INSERT INTO weather (city, temp, humidity, description) 
        VALUES (%s, %s, %s, %s)
    """, (weather_data["city"], weather_data["temp"], weather_data["humidity"], weather_data["description"]))
    
    conn.commit()
    cur.close()
    conn.close()

# Define the DAG
with DAG(
    dag_id="weather_pipeline_nashik",
    start_date=datetime(2025, 9, 21),
    schedule_interval="@daily",
    catchup=False,
    tags=["weather", "nashik"]
) as dag:

    fetch_weather_task = PythonOperator(
        task_id="fetch_weather",
        python_callable=fetch_weather
    )
