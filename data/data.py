import os
from bs4 import BeautifulSoup
import requests
import json
import csv
import time

if not os.path.isdir('data'):
    os.mkdir('data')
dir = os.getcwd()+'/data/'

store_list = []
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
    "cookie": "NNB=2YKK4JEFXEGGG; BMR=s=1661779466480&r=https%3A%2F%2Fpost.naver.com%2Fviewer%2FpostView.naver%3FvolumeNo%3D34132115%26memberNo%3D55643340&r2=; page_uid=82397a98-dda2-4d86-b0f7-b3d8947f1c94"
}
loca = ['%eb%a1%af%eb%8d%b0%eb%a0%8c%ed%84%b0%ec%b9%b4']
for lo in loca:
    time.sleep(3)
    print(lo)
    for i in range(1, 16):
        time.sleep(0.5)
        url = 'https://map.naver.com/v5/api/search?caller=pcweb&query='+lo+'%20%EB%A7%9B%EC%A7%91&type=all&searchCoord=127.2510549;36.3504396&page={0}&displayCount=20&isPlaceRecommendationReplace=true&lang=ko'.format(str(i))
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            jsonObj = json.loads(soup.text)
            stores = jsonObj['result']['place']['list']
            for store in stores:
                store_list.append(
                    [store['name'], store['tel'], store['address'], store['thumUrl'], store['x'], store['y']])
        except:
            print('오류:',lo, i)

for store in store_list:
    print(store)

fields = ['REST_NAME','REST_TEL','REST_ADDRESS','REST_THUMURL','REST_X','REST_Y']

with open('total.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(store_list)