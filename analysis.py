import sqlite3

def run_query(query, desc):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    print(f"\n {desc}")
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


q2 = """
SELECT type, COUNT(*) as total
FROM netflix
GROUP BY type
ORDER BY total DESC;
"""

q3 = """
SELECT country, COUNT(*) as total
FROM netflix
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total DESC
LIMIT 10;
"""
# Run queries
run_query(q1, "Top 10 Years with Most Releases")
run_query(q2, "Movies vs TV Show Count")
run_query(q3, "Top 10 Countries by Content Count")
