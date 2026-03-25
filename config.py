import os
from dotenv import load_dotenv

load_dotenv()
# API_KEY = os.getenv("API_KEY")
# CITY = "Phnom Penh"

DB_CONFIG = {
  "host": "localhost",
  "database": "weather_db",
  "user":"postgres",
  "password":os.getenv("DB_PASSWORD")
}