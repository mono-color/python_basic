import os
import sys
from day5 import mydb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def fn_item_set():

    i = 1
    while True:
        urls = "https://hdex.co.kr/category/all/116?page={0}".format(str(i))
        i += 1
        # 옵션 생성
        options = webdriver.ChromeOptions()
        # 창 숨기는 옵션 추가
        options.add_argument("headless")

        driver = webdriver.Chrome('../day4/chromedriver', options=options)
        driver.implicitly_wait(3)
        driver.get(urls)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup.prettify())
        db = mydb.Mydb()

        lis = soup.select('.prdList > li')
        # print(type(item_data))
        item_data = []
        for li in lis:
            # print(li.text)
            img = li.select_one('img')
            src = img.get('src')
            name_span = li.select_one('.description .name a > span:last-child')
            name = name_span.text
            price_span = li.select_one('.display할인판매가 > span')
            price = price_span.text.replace('원', '')
            code_str = li.get('id').split('_')
            code = code_str[1]
            # print([name, price, code, src])
            item_data.append([name, price, code, src])
        # print(item_data)
        sql = """INSERT INTO gymwear (SEQ, PROD_NAME, PROD_PRICE
                        , PROD_CODE, PROD_IMG) VALUES(gymwear_seq.nextval, :1, :2, :3, :4
                )"""
        cnt = db.fn_insert_list(sql, item_data)
        print(cnt, '건 저장됨')
        if cnt == 0:
            break


fn_item_set()
