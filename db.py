import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect():
    return psycopg2.connect(
        host="localhost",
        database="weather_db",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )