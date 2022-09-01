from telnetlib import EC

import cx_Oracle
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait

from day5 import mydb
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

db = mydb.Mydb()
brand_list = []
sql = "SELECT comm_nm FROM comm_code where comm_parent like 'BN00'"
# conn = cx_Oracle.connect('usedcar', 'oracle', 'localhost:1521/XE', encoding='utf-8')
# with conn:
#     cur
brands = db.get_select(sql)
for i in range(len(brands)):
    brand = brands[i][0]
    brand_list.append(brand)
# print(brand_list)

url = "https://auto.daum.net/"
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('../day4/chromedriver', options=options)
driver.implicitly_wait(2)
driver.get(url)
time.sleep(1)

car_main = BeautifulSoup(driver.page_source, 'html.parser')
list_brand = car_main.find(class_='list_brand')
lis = list_brand.select('li')
# cnt = 0
# print(lis)
for i in range(len(lis)):

    brand_name = lis[i].text
    # cnt += 1
    if brand_name in brand_list:
        print(lis[i])
        driver.find_element(By.CLASS_NAME, 'btn_brand').click()
        driver.find_element(By.CSS_SELECTOR, '.list_brand > li:nth-child({}) > a'.format(str(i + 1))).click()
        print(brand_name, '클릭')
        while True:
            # start = time.time()
            try:
                more_btn = driver.find_element(By.CLASS_NAME, 'more_wrap').find_element(By.TAG_NAME, 'a')
                more_btn.click()
                print(more_btn.text)
                time.sleep(0.2)
            except:
                print('더보기 다누름')
                break
            # end = time.time()
            # print(end - start, '초 걸림')
        while True:
            driver.find_element(By.CLASS_NAME, 'list_lineup')

        driver.back()
        print('나 뒤로가기 눌렀다')
        time.sleep(1.5)

    # if brand_name == driver.find_element(By.CLASS_NAME, 'link_brand').text:
    #     driver.find_element(By.CLASS_NAME, 'link_brand').click()
    #     print('glgl')
