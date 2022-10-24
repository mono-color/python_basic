import sqlite3
# 조회
conn = sqlite3.connect('./example.db')
cur = conn.cursor()
cur.execute("""SELECT *
            FROM stocks""")
# 커서에서 바로 조회
for row in cur:
    print('1번째:', row)
# for row in cur:
for row in cur:
    print('2번째:', row)
# Fetch 사용
# 1건
rows = cur.fetchone()
# 다건
rows = cur.fetchmany()
# 전체
rows = cur.fetchall()
print(rows)
conn.close()