import pandas as pd
from config import DATA_PATH

def load_data(path=DATA_PATH):
    """Load CSV data into a DataFrame."""
    df = pd.read_csv(path)
    print(f"[Loader] ✅ Loaded {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"[Loader] Columns: {list(df.columns)}")
    return df