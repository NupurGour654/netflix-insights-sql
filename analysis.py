import sqlite3

def run_query(query, desc):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    print(f"\n🔍 {desc}")
    for row in cursor.execute(query):
        print(row)
    conn.close()
