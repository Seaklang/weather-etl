# 🌦️Weather ETL Pipeline

This project is a simple ETL (Extract, Transform, Load) pipeline that collects real-time weather data from an API, processes it using Python, and stores it in a PostgreSQL database.

---

##  Project Overview

The pipeline performs the following steps:

1. **Extract**: Fetches weather data from the Open-Meteo API
2. **Transform**: Cleans and structures the data using pandas
3. **Load**: Inserts the processed data into PostgreSQL

---

## Architecture

API → Python → pandas → PostgreSQL

---

## Tech Stack

* Python
* pandas
* requests
* PostgreSQL
* psycopg2

---

## Project Structure

```
weather-etl/
├── etl.py          # Main ETL pipeline
├── db.py           # Database connection
├── .env            # Environment variables (not pushed)
├── .gitignore      # Ignore sensitive files
├── requirements.txt
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/weather-etl.git
cd weather-etl
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```
DB_PASSWORD=your_postgres_password
```

---

### 5. Setup PostgreSQL

Run the following SQL:

```
CREATE DATABASE weather_db;

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    temperature FLOAT,
    windspeed FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 6. Run the ETL pipeline

```
python etl.py
```

---

## Example Output

```
temperature | windspeed | created_at
------------|-----------|---------------------
24.2        | 11.0      | 2026-03-25 ...
```

---

## Features

* Real-time API data extraction
* Data transformation using pandas
* PostgreSQL integration
* Modular code structure

---

## Future Improvements

* Add multiple locations
* Schedule pipeline (Airflow / cron)
* Add logging system
* Build dashboard for visualization

---

## Author

Developed as part of a data engineering learning project.
