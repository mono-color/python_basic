# 가변길이 파라미터
# 함수의 입력 파라미터의 갯수를 0~ n개로 받을 수 있다.
import random


def fn_total(*num):
    tot = 0
    for n in num:
        tot += n
    return tot


def fn_sum_mul(flag, *args):
    if flag == 'sum:':
        result = 0
        for i in args:
            result = result + i
    elif flag == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result


print(fn_total(1, 1, 2))
print(fn_total(1, 1, 2, 5, 6, 7))
print(fn_total())


