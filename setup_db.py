import sqlite3
import pandas as pd
# Load CSV
df = pd.read_csv("data/netflix.csv")

# Clean column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# Create SQLite DB
conn = sqlite3.connect("netflix.db")
df.to_sql("netflix", conn, if_exists="replace", index=False)

print("[INFO] Database 'netflix.db' created with 'netflix' table.")
conn.close()
