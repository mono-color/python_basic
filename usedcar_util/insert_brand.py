import re
import requests
from bs4 import BeautifulSoup as bs
from day5 import mydb

result = []
db = mydb.Mydb()
url = "https://auto.daum.net/"
response = requests.get(url)
soup = bs(response.text, 'html.parser')
cnt = 1
for li in soup.select("ul.list_brand > li"):
    name = li.select_one("a").text
    sql = """INSERT INTO comm_code (comm_cd, comm_nm, comm_parent, comm_ord)
        VALUES ('BN'||LPAD('{}', 2, 0), :v1, 'BN00', :v2)""".format(str(cnt))
    db.fn_insert(sql, [name, cnt])
    cnt += 1





