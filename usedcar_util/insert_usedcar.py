import requests
from bs4 import BeautifulSoup as bs
from day5 import mydb


def get_car_ids() -> list:
    result = []
    for num in range(0, 3080, 20):  # TODO 범위 바꿔주자
        url = "http://api.encar.com/search/car/list/premium"
        params = {
            "count": "true",
            "q": "(And.Hidden.N._.CarType.Y.)",
            "sr": "|ModifiedDate|{}|20".format(str(num))
        }
        response = requests.get(url, params=params)
        data = response.json()
        search_data = data["SearchResults"]
        try:
            for car_info in search_data:
                id = car_info["Photo"].split('/')[-1].replace('_', '')
                result.append(id)
        except Exception as e:
            pass
    # print(result)
    return result


def get_car_information(car_id) -> dict:
    print("[car_id]:{}".format(car_id))
    result = {}
    try:
        print('자 갖고 오자')

        url = "http://www.encar.com/dc/dc_cardetailview.do"
        print('요긴 오땡?')
        params = {
            "method": "ajaxInspectView",
            "rgsid": "{}".format(str(car_id)),
            "sdFlag": "N"
        }
        response = requests.get(url, params=params)
        print('요긴 오땡?22')
        try:
            datas = response.json()[0]["inspect"]
            print('요긴 오땡?333')
            temp = datas["carSaleDto"]
            print('요긴 오땡?4444')
            result = {
                "id": str(temp["carId"]),
                "reg_date": str(temp["regDt"]["year"])[-2:]
                            + "-" + str(temp["regDt"]["month"]).zfill(2)
                            + "-" + str(temp["regDt"]["date"]).zfill(2),
                "brand": temp["manufacturerNm"],
                "name": temp["manufacturerNm"] + ' ' + temp["modelNm"],
                "size": temp["categoryNm"],
                # "type": temp[""],  #TODO 타입 넣어주기 cars테이블 자료 비교해서
                # "eff": temp[""],
                "power": temp["fuelNm"],
                # "code": datas["carSaleDto"][""],
                "price": temp["price"],
                "kil": temp["mileage"],
                "age": temp["adminYear"]
                # "del": datas["carSaleDto"][""]
            }
        except Exception as e:
            print(e)
            print('아니 여긴가?')
            pass

    except Exception as e:
        print(e)
        print('설마 여기도?')
        pass
    return result


if __name__ == "__main__":
    ids = get_car_ids()
    print(ids)
    db = mydb.Mydb()
    sql = """INSERT INTO car_sell (car_id, car_reg_date, car_brand, car_name
                , car_size, car_power
                , car_price, car_kil, car_age) VALUES (
                :v0, :v1, :v2, :v3, :v4, :v5, :v6, :v7 :v8, :v9)"""

    error = ['33159692', '32163781', '33218221', '28557008', '32155505', '31808839', '31189267', '33159692', '33132520',
             '33080869', '31432127', '29489791', '32778009', '32777821', '32421183', '33034962', '32839108', '32601512',
             '33157396', '32900220', '33053916', '33128647', '33185324', '33218212', '31639738', '32848061', '31634360',
             '33178022', '33186151', '33204194', '33207818', '33207818', '32458683', '32906196', '32947841', '33039608',
             '32665624', '33067633', '33137874', '32301320', '32163781', '31556789', '31556789', '33068148', '33145799',
             '33222410', '33198758', '33222410', '33141162', '33046423', '33218221', '32857643', '32987712', '33011223',
             '32801327', '32864091', '33174557', '33216381', '33022488', '33008405', '33190854', '33222410', '33036278',
             '33203221', '33213323', '32792671', '32799959', '33203240', '33212629', '31355364', '32406690', '32582096',
             '32839573', '32917323', '32970491', '32970491', '33157396', '33186151', '33204826', '33204826', '33218212',
             '31732557', '32822716', '32637874', '32601306', '33145043', '33192667', '32831971', '33114075', '33222951',
             '33226042', '33168333', '33224463', '33213834', '33222933', '33203955', '32951470', '32971165', '33134855',
             '33134855', '33187893', '33203971', '31852698', '32796474', '32701364', '33144935', '33144935', '33196311',
             '33204383', '32524312', '32141060', '33171921', '33171921', '33194306', '31841122', '32085916', '32085916',
             '32890296', '33042344', '31185714', '31185714', '33159180', '33187067', '33192931', '33203892', '33197017',
             '33196436', '33196246', '32367940', '32804946', '31995867', '33031562', '33031562', '33203221', '33222107',
             '26402475', '33224414', '32903218', '33218287', '33196045', '33109633', '33171652', '32888000', '33224463',
             '33222938', '33222322', '32805448', '32626238', '33189094', '33213834', '33001927', '33194209', '33210901',
             '32910922', '32944530', '32956695', '33169840', '33004023', '33217173', '32996989', '33050430', '31995867',
             '31995867', '32779050', '33080051', '33079988', '33169442', '33204383', '32786320', '33079791', '32798725',
             '32996217', '33078060', '33079721', '33143106', '33206990', '33213541', '28582674', '32141060', '33080219',
             '33080102', '33091044', '33224404', '33121617', '33195964', '33202022']
    dataset = set(ids) - set(error)
    ids = list(dataset)

    for code in ids:
        try:
            print('=' * 100, ':', code)
            result = get_car_information(code)
            insert = []
            # print(code)
            # print(result)
            try:
                for key, val in result.items():
                    insert.append(val)
            except:
                pass
            print(insert)
            try:
                db.fn_insert(sql, insert)
                print(code, ' 저장됨')
            except Exception as e:
                print(str(e))
                pass
        except Exception as e:
            print('오류다!!!!!!!!!!!',str(e))

        # try:
        #     db.fn_insert(sql, insert)
        #     print(code, ' 저장됨')
        # except Exception as e:
        #     print("인서트 안됐다")
        #     pass

