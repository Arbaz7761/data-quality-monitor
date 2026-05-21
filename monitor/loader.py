import pandas as pd
import os

SUPPORTED_FORMATS = ['.csv', '.json', '.parquet', '.xlsx', '.xls']

def load_data(path):
    """Load data from CSV, JSON, Parquet or Excel file."""

    # Check file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    # Get file extension
    ext = os.path.splitext(path)[1].lower()

    # Check supported format
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {ext}. Supported: {SUPPORTED_FORMATS}")

    # Load based on format
    if ext == '.csv':
        df = pd.read_csv(path)
        format_name = "CSV"

    elif ext == '.json':
        df = pd.read_json(path)
        format_name = "JSON"

    elif ext == '.parquet':
        df = pd.read_parquet(path)
        format_name = "Parquet"

    elif ext in ['.xlsx', '.xls']:
        df = pd.read_excel(path)
        format_name = "Excel"

    print(f"[Loader] ✅ Format detected: {format_name}")
    print(f"[Loader] ✅ Loaded {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"[Loader] Columns: {list(df.columns)}")

    return df