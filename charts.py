import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
# Query runner to return DataFrame
def fetch_df(query):
    conn = sqlite3.connect("netflix.db")
    df_result = pd.read_sql_query(query, conn)
    conn.close()
    return df_result

# Queries
q1 = """SELECT release_year, COUNT(*) as total FROM netflix WHERE release_year IS NOT NULL GROUP BY release_year ORDER BY release_year;"""
q2 = """SELECT type, COUNT(*) as total FROM netflix GROUP BY type;"""
q3 = """SELECT country, COUNT(*) as total FROM netflix WHERE country IS NOT NULL GROUP BY country ORDER BY total DESC LIMIT 10;"""

