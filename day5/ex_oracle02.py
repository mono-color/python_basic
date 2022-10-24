import mydb


db = mydb.Mydb()
print(db.conn.version)
sql = """ select * from member"""
sql2 = """ select * from member where mem_name like '%'||:1||'%' """
mem_list = db.get_select(sql)
mem_list2 = db.get_select_param(sql2, ['김'])
# print(mem_list)
# print(mem_list2)
cnt = db.fn_insert("""INSERT INTO stocks(seq, item_code, stock_name, close_price)
                VALUES (1, :1, :2, :3)
""", [10000, '테스트', 1000.95])
print(cnt)
# seq 사용할 시퀀스 생성(1~999999)
# 4일날 했던 https://m.stock.naver.com
# KOSPI의 현재 주가를 stocks 테이블에 insert 하시오
# 함수로 구현 fn_now_kospi_stock()
