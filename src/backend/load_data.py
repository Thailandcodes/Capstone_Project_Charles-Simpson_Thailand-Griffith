import csv
from src.backend.database import get_connection, create_table


CSV_FILE = "src/backend/climate.csv"


def load_csv_data():
    create_table()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM climate_data")

    with open(CSV_FILE, "r", encoding="latin-1") as file:
        reader = csv.DictReader(file)

        for row in reader:
            country = row["Area"]
            month = row["Months"]
            element = row["Element"]

            for column, value in row.items():
                if column.startswith("Y") and value:
                    year = int(column.replace("Y", ""))

                    cursor.execute(
                        """
                        INSERT INTO climate_data
                        (country, month, element, year, value)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (country, month, element, year, float(value))
                    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    load_csv_data()
