# 라이브러리 설치
# pip install 라이브러리이름
# 문자열 곱하기
abc = 'hi'
print(abc*10)
print(type(abc))
text='''
    안녕하세요
    띄어쓰기 있음
'''
print(text)

# # 조건문
# num = int(input('숫자를 입력해주세요:'))
# if num < 10:
#     print('한자리 수')
# elif num < 180:
#     print('두자리 수')
# else:
#     pass
# 반복문 while
# while True:
#
#
#
#
#  for
# 1
data = [1, 2, 3, 5]
for i in data:
    print(i)
# 2 index와 value에 접근
for i, v in enumerate(data):
    print(i,'번째: ', v)
# 3 단순 횟수
for i in range(3):
    print(data[i])