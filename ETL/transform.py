from extract import extract_data
from openpyxl import load_workbook
import pandas as pd

def transform_data(file_path):
    data = extract_data(file_path)
    
    data = pd.read_csv(file_path, sep=",", encoding='utf-8')

    data["Paciente"] = data["Paciente"].str.lower()
    data["Celular"] = data["Celular"].str.replace('-', '').str.replace(' ', '').str.replace('(', '').str.replace(')', '')
    return data