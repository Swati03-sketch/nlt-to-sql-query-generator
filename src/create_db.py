import sqlite3
from pathlib import Path

DB_PATH = Path("data/company.db")
def createDB(path = DB_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    cursor = conn.cursor()  # cursor object manages the interaction between database and application
    create_table = "CREATE TABLE IF NOT EXISTS Users(" \
    "Id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "NAME TEXT NOT NULL," \
    "AGE INTEGER NOT NULL);" 
    cursor.execute(create_table)

    rows = [
        (1, "Mohit", 23),
        (2, "Shital", 21),
        (3, "Ankit", 25),
        (4, "Pooja", 22),
        (5, "Ravi", 24)
    ]
    cursor.executemany("INSERT INTO Users VALUES(?, ?, ?);", rows)
    conn.commit()
    conn.close()
    print(f"Database and Table created at {path}")

if __name__ == "__main__":
    createDB()