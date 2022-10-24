import json
import mydb
import requests
from bs4 import BeautifulSoup

# 작성자 : 임동성
def fn_now_kospi_stock():
    db = mydb.Mydb()
    stock_data = []
    for i in range(1, 10):
        url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={0}&pageSize=50'.format(str(i))
        res = requests.get(url)
        # print(res.text)
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(soup)
        jsonObj = json.loads(soup.text)
        print(jsonObj)
        stock_list = jsonObj['stocks']
        # print(type(stock_list))  # list임
        for stock in stock_list:
            stock_data.append([stock['itemCode'], stock['stockName'], stock['closePrice']])
            print(stock_data)

        print(stock_data)
        sql = """INSERT INTO stocks (SEQ, ITEM_CODE, STOCK_NAME
                , CLOSE_PRICE) VALUES(stock_seq.nextval, :1, :2, :3
        )"""

        cnt = db.fn_insert_list(sql, stock_data)
        print(cnt, '건 저장됨')


fn_now_kospi_stock()
