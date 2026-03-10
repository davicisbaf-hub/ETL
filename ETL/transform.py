from .extract import extract_data
import pandas as pd

def transform_data(raw_file_path):
    data = extract_data(raw_file_path)
    
    data = pd.read_csv(raw_file_path, sep=",", encoding='utf-8')

    data["Paciente"] = data["Paciente"].str.lower()
    
    data["Celular"] = data["Celular"].str.replace('-', '').str.replace(' ', '').str.replace('(', '').str.replace(')', '')
    
    data["Data / Hora"] = data["Data / Hora"].str.split(' ').str[0]
    data["Data / Hora"] = pd.to_datetime(data["Data / Hora"], format='%d/%m/%Y', errors='coerce')

    data = data.rename(columns={
        "Paciente": "paciente",
        "Celular": "celular",
        "Procedimento": "procedimento",
        "Data / Hora": "data_hora",
        "Prestador": "prestador",
        "Profissional": "profissional",
        "Município": "municipio",
        "UBS": "ubs",
        "Valor regional": "valor_regional",
        "Valor SUS": "valor_sus",
        "Contraste": "contraste",
        "Sedação": "sedacao",
        "Valor total": "valor_total"
    })

    return data