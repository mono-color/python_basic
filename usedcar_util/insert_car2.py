import re
import requests
from bs4 import BeautifulSoup as bs
from day5 import mydb


def get_brands() -> list:
    result = []
    url = "https://auto.daum.net/"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    for li in soup.select("ul.list_brand > li"):
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
    response = requests.get(url, params=params)
    data = response.json()
    for i in data["data"]:
        car_type = i["etcInfo"]["bodyType"]
        if car_type == "VAN":
            car_type = "RV"
        result.append({
            "brand": i["parentCluster"]["title"],
            "name": i["title"],
            "size": i[""],
            "type": car_type,
            "power": i["etcInfo"]["powerTrain"],
            "efficiency": i["etcInfo"]["maxEfficiency"],
            "code": i["etcInfo"]["orgId"],
            "img": i["image"]["exterior"]
        })
    return result


db = mydb.Mydb()

if __name__ == "__main__":
    brands = get_brands()
    for brand in brands:
        for car in get_cars(brand["brand_id"]):
            sql = """INSERT INTO cars (car_brand, car_name, car_type, car_effic, car_power, car_code, car_img)
             VALUES (:v0, :v1, :v2, :v3, :v4, :v5, :v6)"""
            db.fn_insert(sql, [car["brand"], car["name"], car["type"], car["efficiency"], car["power"], car["code"],
                               car["img"]])
        print(brand["name"], ' 저장완료')
