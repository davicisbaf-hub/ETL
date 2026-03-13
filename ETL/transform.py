from .extract import extract_data
import pandas as pd

def transform_data(raw_file_path):
    data = extract_data(raw_file_path)
    
    data = pd.read_csv(raw_file_path, sep=",", encoding='utf-8')

    data["Paciente"] = data["Paciente"].str.lower()
    
    data["Celular"] = data["Celular"].str.replace('-', '').str.replace(' ', '').str.replace('(', '').str.replace(')', '')
    
    data["Data / Hora"] = data["Data / Hora"].str.split(' ').str[0]
    data["Data / Hora"] = pd.to_datetime(data["Data / Hora"], format='%d/%m/%Y', errors='coerce')

    data['codigo_procedimento'] = data['Procedimento'].str.split(' - ').str[0]
    data['Procedimento'] = data['Procedimento'].str.split('- ').str[1]

    data["Procedimento"] = data["Procedimento"].str.rsplit(" (", n=1).str[0]


    data["Valor regional"] = data["Valor regional"].str.replace('R$ ', '')
    data["Valor SUS"] = data["Valor SUS"].str.replace('R$ ', '')
    data["Contraste"] = data["Contraste"].str.replace('R$ ', '')
    data["Sedação"] = data["Sedação"].str.replace('R$ ', '')
    data["Valor total"] = data["Valor total"].str.replace('R$ ', '')

    data = data.iloc[:-1].reset_index(drop=True)

    data = data.rename(columns={
        "Paciente": "paciente",
        "Celular": "celular",
        "codigo_procedimento": "codigo_procedimento",
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

    data = data[
        [
            "paciente", 
            "celular", 
            "codigo_procedimento", 
            "procedimento", 
            "data_hora", 
            "prestador", 
            "profissional", 
            "municipio", 
            "ubs", 
            "valor_regional", 
            "valor_sus", 
            "contraste", 
            "sedacao", 
            "valor_total"
        ]
    ]

    return data