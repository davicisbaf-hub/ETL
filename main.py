from ETL.load import load_data

processed_data = "data/processed/processed.csv"

if __name__ == "__main__":
    processed_data = "data/processed/processed.csv"
    load_data(processed_data, "database/opera.db")
