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
