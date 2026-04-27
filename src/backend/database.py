import sqlite3

DATABASE_NAME = "climate.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS climate_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT NOT NULL,
        year INTEGER NOT NULL,
        temperature REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_country_year
    ON climate_data (country, year)
    """)

    conn.commit()
    conn.close()