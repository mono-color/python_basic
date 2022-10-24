import requests as rq
from bs4 import BeautifulSoup as bs
from day5 import mydb
import random

db = mydb.Mydb()

brand_list = ['현대', '기아', '쌍용', '르노코리아', '쉐보레', '제네시스', 'BMW', '벤츠', '아우디', '폭스바겐', '포르쉐', '람보르기니']


def get_brands() -> list:
    result = []
    url = "https://auto.daum.net/"
    response = rq.get(url)
    soup = bs(response.text, "html.parser")
    for li in soup.select("ul.list_brand > li"):
        if li.select_one("a").text in brand_list:
            result.append({
                "name": li.select_one("a").text,
                "brand_id": li.select_one("a")["href"].split("/")[-1]
            })
    return result


def get_cars(brand_id=str) -> list:
    result = []
    url = "https://auto.daum.net/prx/mc2/v2/clusters.json"
    params = {
        "pageSize": "200",
        "page": "1",
        "sortField": "etcInfo.latestReleaseDate",
        "sortValue": "desc",
        "service": "auto",
        "type": "models",
        "filterKey": "etcInfo.brand",
        "filterVal": brand_id
    }
    response = rq.get(url, params=params)
    data = response.json()
    for i in data["data"]:
        max_price = i["ranking"]["maxPrice"]
        min_price = i["ranking"]["minPrice"]
        car_price = int((max_price + min_price)/2 / 300)
        car_eff = i["etcInfo"]["maxEfficiency"]
        car_year = int(i["etcInfo"]["years"].split(",")[-1])
        car_brand = i["parentCluster"]["title"]
        if car_price == 0 or car_eff == 0 or car_year <= 2019:
            pass
        else:
            car_price = str(car_price)
            car_price = car_price[0:-3]+"000"
            car_size = i["etcInfo"]["segment"]
            car_type = i["etcInfo"]["bodyType"]
            if car_type == "VAN":
                car_type = "RV"
            if car_size == "E":
                car_size = "대형"
            elif car_size == "D":
                car_size = "중형"
            elif car_size == "C":
                car_size = "소형"
            else:
                car_size = "경형"
            ran = random.randint(1, 10)
            ran_for = random.randint(1, 10)
            if car_brand in ["BMW", "벤츠", "아우디", "폭스바겐", "포르쉐", "람보르기니"]:
                if ran_for >= 9:
                    if car_size in ["경형", "소형", "중형"]:
                        if ran >= 3:
                            # 확률로 값 넣기
                            result.append({
                                # 차량id
                                "name": i["title"],
                                "brand": car_brand,
                                "type": car_type,
                                "size": car_size,
                                "power": i["etcInfo"]["powerTrain"],
                                "efficiency": car_eff + 'km/h',
                                "price": car_price,
                                "img": i["image"]["exterior"]
                                # 판매업체명
                            })
                    elif car_size == "대형":
                        if ran >= 5:
                            result.append({
                                # 차량id
                                "name": i["title"],
                                "brand": i["parentCluster"]["title"],
                                "type": car_type,
                                "size": car_size,
                                "power": i["etcInfo"]["powerTrain"],
                                "efficiency": car_eff + 'km/h',
                                "price": car_price,
                                "img": i["image"]["exterior"]
                                # 판매업체명
                            })
            elif car_size in ["경형", "소형", "중형"]:
                if ran >= 3:
                    # 확률로 값 넣기
                    result.append({
                        # 차량id
                        "name": i["title"],
                        "brand": car_brand,
                        "type": car_type,
                        "size": car_size,
                        "power": i["etcInfo"]["powerTrain"],
                        "efficiency": car_eff+'km/h',
                        "price": car_price,
                        "img": i["image"]["exterior"]
                        # 판매업체명
                    })
            elif car_size == "대형":
                if ran >= 5:
                    result.append({
                        # 차량id
                        "name": i["title"],
                        "brand": i["parentCluster"]["title"],
                        "type": car_type,
                        "size": car_size,
                        "power": i["etcInfo"]["powerTrain"],
                        "efficiency": car_eff + 'km/h',
                        "price": car_price,
                        "img": i["image"]["exterior"]
                        # 판매업체명
                    })

    return result


def get_company():
    sql = "SELECT CC_NAME FROM car_company"
    com_names = db.get_select(sql)
    name_list = []
    for i in com_names:
        name_list.append(i[0])
    return name_list


if __name__ == "__main__":
    brands = get_brands()
    company_names = get_company()
    for company in company_names:
        print(company)
        for brand in brands:
            print(brand['name'])
            print(get_cars(brand["brand_id"]))
            print(len(get_cars(brand["brand_id"])))
            cars = get_cars(brand["brand_id"])
            for car in cars:
                temp = [
                    car["name"], car["brand"], car["type"], car["size"], car["power"]
                    , car["efficiency"], car["price"], car["img"], company
                ]
                sql = """
                    INSERT INTO rent_car (
                        car_id    , car_name    , car_brand
                        , car_type    , car_size    , car_power
                        , car_eff    , car_price    , car_img    , car_company
                    ) VALUES (
                        'RC'||LPAD(rent_car_id_seq.nextval, 5, '0')    , :v1    , :v2    , :v3
                        , :v4    , :v5    , :v6    , :v7
                        , :v8    , :v9
                    )
                """
                db.fn_insert(sql, temp)
                print("삽입 완료")
        # for car in get_cars(brand["brand_id"]):
        #     sql

