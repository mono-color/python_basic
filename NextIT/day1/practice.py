import random

count = int(input('로또 숫자는 몇개??'))
for i in range(count):
    setLotto = set()
    while len(setLotto) < 6:
        ran = random.randint(1, 45)
        setLotto.add(ran)
    print(setLotto)