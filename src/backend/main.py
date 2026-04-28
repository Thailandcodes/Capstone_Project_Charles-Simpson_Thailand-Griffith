from src.backend.gcs_utils import upload_file_to_gcs, get_gcs_file_url
from fastapi import FastAPI, HTTPException
from src.backend.database import create_table, get_db_connection

app = FastAPI(title="A Dying Planet Climate API")

create_table()


@app.get("/")
def home():
    return {"message": "Climate API running"}


@app.get("/data")
def get_all_data():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM climate_data").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/data/{country}")
def get_country_data(country: str):
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT * FROM climate_data WHERE country = ? ORDER BY year",
        (country,)
    ).fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="Country not found")

    return [dict(row) for row in rows]


@app.post("/data")
def add_data(country: str, year: int, temperature: float):
    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO climate_data (country, year, temperature)
        VALUES (?, ?, ?)
        """,
        (country, year, temperature)
    )
    conn.commit()
    conn.close()

    return {
        "message": "Data added successfully",
        "country": country,
        "year": year,
        "temperature": temperature
    }


@app.delete("/data/{record_id}")
def delete_data(record_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM climate_data WHERE id = ?", (record_id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Record not found")

    conn.close()
    return {"message": "Data deleted successfully"}

@app.post("/files/upload")
def upload_file(bucket_name: str, source_file: str, destination_blob: str):
    return upload_file_to_gcs(bucket_name, source_file, destination_blob)


@app.get("/files/url")
def get_file_url(bucket_name: str, blob_name: str):
    return get_gcs_file_url(bucket_name, blob_name)