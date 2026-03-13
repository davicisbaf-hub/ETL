from .transform import transform_data
import pandas as pd

pd.DataFrame.to_csv(
    transform_data("data/raw/Procedimentos agendados  Marque fácil.csv"), "data/processed/processed.csv", index=False
)