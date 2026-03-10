from ETL.load import load_data
import pandas as pd

processed_data = "data/processed/processed.csv"

load_data(processed_data, "database/opera.db")