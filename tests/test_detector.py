import pandas as pd
import numpy as np
from monitor.detector import check_nulls, check_duplicates, check_outliers

def test_null_detection():
    """Test that null values are detected correctly."""
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": [1, 2, 3]
    })
    result = check_nulls(df)
    assert "a" in result
    assert result["a"] == round(1/3 * 100, 2)
    assert "b" not in result
    print("✅ test_null_detection passed!")

def test_duplicate_detection():
    """Test that duplicate rows are detected correctly."""
    df = pd.DataFrame({
        "a": [1, 1, 2],
        "b": [3, 3, 4]
    })
    result = check_duplicates(df)
    assert result == 1
    print("✅ test_duplicate_detection passed!")

def test_no_outliers():
    """Test that clean data has no outliers."""
    df = pd.DataFrame({
        "a": [10, 11, 10, 12, 11]
    })
    result = check_outliers(df)
    assert result == {}
    print("✅ test_no_outliers passed!")