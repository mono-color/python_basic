from day5 import mydb

db = mydb.Mydb()


sql_select_member = """SELECT
                        mem_name    , mem_id    , mem_pass    , mem_age    , mem_sex
                        , mem_job    , mem_hobby   , mem_phone    , mem_mail    , mem_del
                    FROM
                        members"""
sql_select_car = """SELECT rownum,
                        car_id    , car_reg_date    , car_brand    , car_name    , car_size
                        , car_type    , car_effic    , car_power    , car_code    , car_price
                        , car_kil    , car_age    , car_del
                    FROM
                        car_sell"""

sql_insert_history = """INSERT INTO sell_history (
                            car_brand    , car_name    , car_size    , car_type
                            , car_price    , car_age    , buyer_id    , buyer_age
                            , buyer_sex    , buyer_job    , buyer_hobby
                        ) VALUES (
                            :v0    , :v1    , :v2    , :v3
                            , :v4    , :v5    , :v6    , :v7
                            , :v8    , :v9    , :v10
                        )"""
members = db.get_select(sql_select_member)
cars = db.get_select(sql_select_car)
# for i in cars:
#     print(i)
while True:
    for mem in members:
        try:
            print(mem)
            text = int(input('구매차량 번호를 입력하세요: '))

            car = cars[text-1]
            buy_car = [car[3], car[4], car[5], car[6], car[10], car[12], mem[1], mem[3], mem[4], mem[5], mem[6]]
            print(buy_car)
            db.fn_insert(sql_insert_history, buy_car)
        except:
            pass




