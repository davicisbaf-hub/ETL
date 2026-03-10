import sqlite3
import pandas as pd

def load_data(processed_data, db_path):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    df = pd.read_csv(processed_data, sep=",", encoding='utf-8')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consolidado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente TEXT,
            celular TEXT,
            procedimento TEXT,
            data_hora DATE,
            prestador TEXT,
            profissional TEXT,
            municipio TEXT,
            ubs TEXT,
            valor_regional REAL,
            valor_sus REAL,
            contraste TEXT,
            sedacao TEXT,
            valor_total REAL
        )
    ''')

    df.to_sql("consolidado", con, if_exists="append", index=False)
    con.close()