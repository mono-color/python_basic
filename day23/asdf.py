import requests
from day5 import mydb

url = "https://apis.data.go.kr/B551011/GoCamping/basedList?MobileOS=AND&MobileApp=fdffd&serviceKey=z6jw1epFn%2F0%2BC7yHzGcCm3VCdzsKPT1EIHx7Jh9Vy2xvv%2F094lLoG6MNSIPj86GO5QcnYMu3GFYjCwjYmWAnCg%3D%3D&_type=json"
param = {
    "numOfRows": 1,
    "pageNo": 1
}
# print('222')
datas = requests.get(url, params=param, verify=False).json()
data = datas["response"]["body"]["items"]["item"]

# data는 리스트 안에 값이 dict
# print(data[0].keys())

# cnt = 0
# for i in data:
#     for key, value in i.items():
#         cnt += 1
#         print(key, value)
#         # print(key, 'varchar2(2000),')
# print(cnt)

# sql = "dsfa"
# sql += "df"
# sql = sql[:len(sql)-1]
# print(sql)

db = mydb.Mydb()