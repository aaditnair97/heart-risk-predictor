import pandas as pd

def load_data(path="data/heart_disease_clean.csv"):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"⚠️ File not found at : {path}")
        return None