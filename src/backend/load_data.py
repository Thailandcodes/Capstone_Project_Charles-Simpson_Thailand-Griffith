import pandas as pd
from src.backend.database import get_db_connection

def load_csv():
    df = pd.read_csv("src/backend/climate.csv")

    conn = get_db_connection()

    df = df[['country', 'year', 'temperature']]  # adjust if needed

    df.to_sql("climate_data", conn, if_exists="append", index=False)

    conn.close()

if __name__ == "__main__":
    load_csv()
    print("Data loaded successfully")