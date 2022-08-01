
# 함수
def fn_name(param):
    return param*10

print(fn_name('hi'))

def fn_name2(param):
    nm = param.split()
    return nm[0], nm[1]

first, last = fn_name2('팽 수') #변수를 하나로 주면 튜플로 인식(키,밸류)
print('성:', first, '이름:', last)