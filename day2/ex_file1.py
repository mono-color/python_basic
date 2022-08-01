import os
# 위치
import shutil

print(os.getcwd())
path = os.getcwd()
file_list = os.listdir(path)
for file in file_list:
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        print('파일: ', file_path)
        if 'delay' in file:
            print("=" * 100, file_path)
            os.remove(file_path)
            print(file_path, "삭제함")
            print("=" * 100)
    if os.path.isdir(file_path):
        #if 'test' in file:
        try:
            print('디렉토리: ', file_path)
            os.rmdir(file_path)
            print(file_path, '디렉토리 삭제됨')
        except Exception as e:
            print(str(e))
            # shutil.rmtree((file_path)) #하위까지 삭제

# 삭제하고 싶은 파일 명을 입력 받아 지우는 함수를 만드시오
# 조건 : 삭제전에 맞는지 물어보고(y/n) y면 삭제 n이면 종료 하는
# (경로는 일단 현재 위치, 괜찮다면 입력받아서)
