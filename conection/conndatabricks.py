import sqlite3
import pandas as pd
from databricks import sql
from dotenv import load_dotenv
import os

load_dotenv()

sqlite_conn = sqlite3.connect("database/opera.db")

df = pd.read_sql_query("""
    SELECT * FROM consolidado
""", sqlite_conn)

sqlite_conn.close()

df.to_csv("conection/dados.csv", index=False)


connection = sql.connect(
    server_hostname=os.getenv("server_hostname"),
    http_path=os.getenv("http_path"),
    access_token=os.getenv("access_token")
)

cursor = connection.cursor()


data = [tuple(x) for x in df.to_numpy()]

query = """
INSERT INTO workspace.default.processed
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

cursor.executemany(query, data)

connection.commit()

cursor.close()
connection.close()

print("ETL concluído 🚀")