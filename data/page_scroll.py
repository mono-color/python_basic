from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# made by GOD 의창

url = "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EB%A0%8C%ED%84%B0%EC%B9%B4/";
# uri= "https://hello-bryan.tistory.com/194"
driver = webdriver.Chrome('../day4/chromedriver')
driver.implicitly_wait(3)
driver.get(url)
# SCROLL_PAUSE_SEC = 1

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
# item_list = driver.find_element(By.CLASS_NAME, 'XUrfU')
# driver.execute_script("arguments[0].scrollIntoView(true)", item_list)

# 스크롤 높이 가져옴
# last_height = driver.execute_script("return document.'body'.scrollHeight")
#
# while True:
#     # 끝까지 스크롤 다운
#     driver.execute_script("arguments[0].scrollIntoView(true)", item_list)
#
#     # 1초 대기
#     time.sleep(SCROLL_PAUSE_SEC)
#
#     # 스크롤 다운 후 스크롤 높이 다시 가져옴
#     new_height = driver.execute_script("return document.'body'.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height










