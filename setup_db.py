import sqlite3
import pandas as pd
# Load CSV
df = pd.read_csv("data/netflix.csv")

# Clean column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
