import cx_Oracle


class Mydb:

    def __init__(self):  # 초기값 세팅
        self.conn = None
        self.get_connection()

    # 소멸자
    def __del__(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(str(e))

    def get_connection(self):
        self.conn = cx_Oracle.connect('proj'
                                      , 'proj'
                                      , '192.168.0.52:1521/XE'
                                      , encoding='utf-8')
        return self.conn

    def get_select(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_select_param(self, query, param):
        cur = self.conn.cursor()
        cur.execute(query, param)
        rows = cur.fetchall()
        cur.close()
        return rows

    # 1건
    def fn_insert(self, query, param):
        cur = self.conn.cursor()
        cur.execute(query, param)
        cnt = cur.rowcount
        cur.close()
        self.conn.commit()
        return cur.rowcount

    # 여러
    def fn_insert_list(self, query, param):
        cur = self.conn.cursor()
        cur.executemany(query, param)
        cnt = cur.rowcount
        cur.close()
        self.conn.commit()
        return cur.rowcount


if __name__ == '__main__':
    print('conn test')
    db = Mydb()
    conn = db.get_connection()
    print(conn.version)
