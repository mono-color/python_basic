import os
from bs4 import BeautifulSoup
import requests
import json
from day5 import mydb
import csv

# if not os.path.isdir('data'):
#     os.mkdir('data')
# dir = os.getcwd() + '/data/'


def make_data_list():
    store_list = []

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
        "cookie": "NNB=2YKK4JEFXEGGG; BMR=s=1661779466480&r=https%3A%2F%2Fpost.naver.com%2Fviewer%2FpostView.naver%3FvolumeNo%3D34132115%26memberNo%3D55643340&r2=; page_uid=82397a98-dda2-4d86-b0f7-b3d8947f1c94"
    }
    url = 'https://map.naver.com/v5/api/search?caller=pcweb&query=%EB%A1%AF%EB%8D%B0%20%EB%A0%8C%ED%84%B0%EC%B9%B4&type=all&searchCoord=127.3894337;36.3252236&page=1&displayCount=85&isPlaceRecommendationReplace=true&lang=ko'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    try:
        jsonObj = json.loads(soup.text)
        stores = jsonObj['result']['place']['list']
        for store in stores:
            store_list.append(
                [store['name'], store['address'],
                 store['x'], store['y'], store['tel'], store['thumUrl'], store['bizhourInfo']])
    except:
        print('오류')
    return store_list


company_list = make_data_list()
db = mydb.Mydb()
sql = """ INSERT INTO car_company (
                 cc_id  ,    cc_name    , cc_add    , cc_mapx
        , cc_mapy    , cc_homepage    , cc_tel    , cc_thum_url
        , cc_biz_hour
    ) VALUES ( 'CC'||LPAD(car_company_id_seq.nextval, 4, '0')   , :v1    , :v2    , :v3
        , :v4    , 'https://www.lotterentacar.net'    , :v5    , :v6
        , :v7   ) """
# print(company_list)
for comp in company_list:
    print(comp)
    db.fn_insert(sql, comp)


# fields = ['REST_ID', 'REST_NAME', 'REST_TEL',
#           'REST_ADDRESS', 'REST_THUMURL', 'REST_BIZHOURINFO', 'REST_X', 'REST_Y']

# with open('car.csv', 'w', newline='') as f:
#     write = csv.writer(f)
#     write.writerow(fields)
#     write.writerows(store_list)

