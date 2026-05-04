import sqlite3

DB_NAME = "climate.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS climate_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT NOT NULL,
            month TEXT NOT NULL,
            element TEXT NOT NULL,
            year INTEGER NOT NULL,
            value REAL
        )
    """)

    conn.commit()
    conn.close()
