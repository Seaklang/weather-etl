import requests
import pandas as pd
from db import connect   # 👈 this is where db.py is used

# -------------------
# Extract
# -------------------
def extract():
    url = "https://api.open-meteo.com/v1/forecast?latitude=11.56&longitude=104.92&current_weather=true"
    response = requests.get(url)
    data = response.json()

    print("Extracted:", data)
    return data

# -------------------
# Transform
# -------------------
def transform(data):
    weather = data["current_weather"]

    df = pd.DataFrame([{
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"]
    }])

    print("Transformed Data:")
    print(df)

    return df

# -------------------
# Load
# -------------------
def load(df):
    conn = connect()   # using db.py
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO weather_data (temperature, windspeed)
            VALUES (%s, %s)
            """,
            (float(row["temperature"]), float(row["windspeed"]))
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded into PostgreSQL!")

# -------------------
# Run ETL
# -------------------
def run_etl():
    data = extract()
    df = transform(data)
    load(df)

if __name__ == "__main__":
    run_etl()