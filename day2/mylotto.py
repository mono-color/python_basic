# 로또함수
import random


def fn_lotto(num):
    lottoList = []
    for i in range(num):
        setLotto = set()
        while len(setLotto) < 6:
            ran = random.randint(1, 45)
            setLotto.add(ran)
        lottoList.append(setLotto)
    return lottoList


print('로또번호들:', fn_lotto(4))
