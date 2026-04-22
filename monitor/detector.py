import pandas as pd
import numpy as np

def check_nulls(df):
    """Find columns with null values."""
    null_pct = df.isnull().mean()
    issues = null_pct[null_pct > 0].to_dict()
    return {col: round(pct * 100, 2) for col, pct in issues.items()}

def check_outliers(df):
    """Detect outliers using Z-score on numeric columns."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    outlier_report = {}
    for col in numeric_cols:
        z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
        outlier_count = (z_scores > 3.0).sum()
        if outlier_count > 0:
            outlier_report[col] = int(outlier_count)
    return outlier_report

def check_duplicates(df):
    """Count duplicate rows."""
    return int(df.duplicated().sum())

def check_schema(df):
    """Return column names and their data types."""
    return df.dtypes.apply(str).to_dict()

def run_all_checks(df):
    """Run all quality checks and return combined report."""
    report = {
        "shape": df.shape,
        "null_percentages": check_nulls(df),
        "outliers": check_outliers(df),
        "duplicate_rows": check_duplicates(df),
        "schema": check_schema(df)
    }
    return report