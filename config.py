import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = "claude-sonnet-4-20250514"
DATA_PATH = "data/sample_data.csv"
NULL_THRESHOLD = 0.10
OUTLIER_THRESHOLD = 3.0