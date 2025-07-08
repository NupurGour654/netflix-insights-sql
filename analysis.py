import sqlite3

def run_query(query, desc):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    print(f"\n🔍 {desc}")
    for row in cursor.execute(query):
        print(row)
    conn.close()

# Queries
q1 = """
SELECT release_year, COUNT(*) as total
FROM netflix
WHERE release_year IS NOT NULL
GROUP BY release_year
ORDER BY release_year DESC
LIMIT 10;
"""
