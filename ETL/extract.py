import pandas as pd

def extract_data(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        return e
    
    