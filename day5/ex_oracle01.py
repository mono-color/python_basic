import cx_Oracle

# pip install cx_Oracle
# conn = cx_Oracle.connect('java', 'oracle', 'localhost:1521/XE')
# print(conn.version)
# with conn:
#     cur = conn.cursor()
#     cur.execute("""SELECT mem_id
#                          , mem_name
#                          , mem_job
#                          , mem_mail
#                     FROM member
#                WHERE mem_name like '%'||:1||'%'
#     """, ['김'])
#     # 이름의 포함 텍스트 입력받아 조회 결과 리턴하는 함수 만들기
#     # input: str, return: list
#
#     rows = cur.fetchall()
#     for i in cur.description:
#         print(i[0])
#     for row in rows:
#         print(row)


def fn_get_mem(name):
    conn = cx_Oracle.connect('java', 'oracle', 'localhost:1521/XE')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT mem_id
                             , mem_name
                             , mem_job
                             , mem_mail
                        FROM member
                   WHERE mem_name like '%'||:1||'%'     
        """, [name])
        rows = cur.fetchall()
    return rows


while True:
    msg = input('이름으로 고객조회:')
    mem_list = fn_get_mem(msg)
    for mem in mem_list:
        print(mem)
