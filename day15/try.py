import os
import sys
from day5 import mydb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

db = mydb.Mydb()
sql = """SELECT  seq, prod_name, prod_price, prod_code, prod_img
        FROM gymwear"""
db.get_select(sql)
print(type(db.get_select(sql)))
print(len(db.get_select(sql)))
for i in range(len(db.get_select(sql))):
    print(db.get_select(sql)[i])
