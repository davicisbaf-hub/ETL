import sqlite3
import pandas as pd

def load_data(processed_data, db_path):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()    

    df = pd.read_csv(processed_data, sep=",", encoding='utf-8')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consolidado (
            paciente TEXT,
            celular TEXT,
            codigo_procedimento TEXT,
            procedimento TEXT,
            data_hora DATE,
            prestador TEXT,
            profissional TEXT,
            municipio TEXT,
            ubs TEXT,
            valor_regional DECIMAL(10, 2),
            valor_sus DECIMAL(10, 2),
            contraste DECIMAL(10, 2),
            sedacao DECIMAL(10, 2),
            valor_total DECIMAL(10, 2)
        )
    ''')

    df.to_sql("consolidado", con, if_exists="append", index=False)    
    con.close() 