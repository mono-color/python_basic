import FinanceDataReader as fdr
import pandas as pd
import datetime
from pandas.tseries.offsets import BDay
# pip install pytimekr
from pytimekr import pytimekr
from ex_stock import *
day = pytimekr.holidays()
# for i in sorted(day):
#     print(i)


def fn_workingday(b_day):
    start = (datetime.datetime.today() - BDay(b_day))
    end = (datetime.datetime.today() - BDay(1))
    print(start)
    red_day = sorted(pytimekr.holidays())
    # 선거일 추가
    red_day.append(datetime.date(2022, 6, 1))
    holiday = []
    for i in red_day:
        check = datetime.datetime.combine(i, datetime.datetime.min.time())
        if start < check and end > check:
            holiday.append(check)
        if holiday:
            start = (datetime.datetime.today() - BDay(b_day + len(holiday)))
    return start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')


start, end = fn_workingday(50)
# print(start, end)
fn_get_stock('005930', start, end)