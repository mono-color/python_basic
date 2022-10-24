from day5 import mydb
import requests


def fn_insert_camp():
    db = mydb.Mydb()
    url = "https://apis.data.go.kr/B551011/GoCamping/basedList?"
    param = {
        "numOfRows": 4000,
        "pageNo": 1,
        "MobileOS": "AND",
        "MobileApp": "fdffd",
        "serviceKey": "z6jw1epFn/0+C7yHzGcCm3VCdzsKPT1EIHx7Jh9Vy2xvv/094lLoG6MNSIPj86GO5QcnYMu3GFYjCwjYmWAnCg==",
        "_type": "json"
    }
    datas = requests.get(url, params=param, verify=False).json()
    data = datas["response"]["body"]["items"]["item"]
    # print(type(data[0]))
    for i in data:
        sql = "INSERT INTO CAMPING_SPOT ("
        for key, value in i.items():
            if key == 'contentId' or key == 'facltNm' or key == 'intro' or key == 'featureNm' or key == 'induty' \
                    or key == 'lctCl' or key == 'doNm' or key == 'sigunguNm' or key == 'addr1' or key == 'addr2' \
                    or key == 'mapX' or key == 'mapY' or key == 'tel' or key == '' or key == 'homepage' \
                    or key == 'resveUrl' or key == 'glampInnerFclty' or key == 'caravInnerFclty' or key == 'sbrsCl' \
                    or key == 'posblFcltyCl' or key == 'exprnProgrm' or key == 'animalCmgCl' or key == 'firstImageUrl':
                sql += key + ","
        sql = sql[:len(sql) - 1]
        sql += ") VALUES ("
        for key, value in i.items():
            if key == 'contentId' or key == 'facltNm' or key == 'intro' or key == 'featureNm' or key == 'induty' \
                    or key == 'lctCl' or key == 'doNm' or key == 'sigunguNm' or key == 'addr1' or key == 'addr2' \
                    or key == 'mapX' or key == 'mapY' or key == 'tel' or key == '' or key == 'homepage' \
                    or key == 'resveUrl' or key == 'glampInnerFclty' or key == 'caravInnerFclty' or key == 'sbrsCl' \
                    or key == 'posblFcltyCl' or key == 'exprnProgrm' or key == 'animalCmgCl' or key == 'firstImageUrl':
                sql += "'" + value + "',"
        sql = sql[:len(sql) - 1]
        sql += ")"
        # print(sql)
        try:
            db.fn_insert_data(sql)
        except:
            print("예외발생")


fn_insert_camp()
