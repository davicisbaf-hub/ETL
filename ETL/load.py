from transform import transform_data
import pandas as pd

def load_data(file_path):
    return transform_data(file_path)

pd.DataFrame.to_csv(load_data('data/raw/Procedimentos agendados  Marque fácil.csv'), 'data/processed/relatório_financeiro.csv',index=False )