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

# Load results
df_year = fetch_df(q1)
df_type = fetch_df(q2)
df_country = fetch_df(q3)

# Chart 1: Line plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='release_year', y='total', data=df_year, marker='o')
plt.title("Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/year_trend.png")
plt.show()

# Chart 2: Bar chart
plt.figure(figsize=(6, 4))
sns.barplot(x='type', y='total', data=df_type, palette='Set2')
plt.title("Content Distribution by Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/type_distribution.png")
plt.show()
