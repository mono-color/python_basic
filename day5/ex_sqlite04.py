# with 사용
import sqlite3
conn= sqlite3.connect('./example.db')
with conn:
    cur = conn.cursor()
    cur.execute("""select * from stocks""")
    rows = cur.fetchall()
    for row in rows:
        print(row)