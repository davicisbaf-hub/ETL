import pandas as pd

def extract_data(raw_file_path):
    try:
        data = pd.read_excel(raw_file_path)
        return data
    except Exception as e:
        return e
    
    