import os

path = os.getcwd()
file_list = os.listdir(path)

for file in file_list:
    file_path = os.path.join(path, file)
    print("file_path : ", file_path)
    print("path : ", path)
    print("file : ", file)
#
# for file in file_list:
#     file_path = os.path.join(path, file)
#     print(file_path)
#     target_file = input('삭제할 파일 입력: (exit:q)')
#     if target_file == 'q':
#         print("종료")
#         break
#     if os.path.isfile(file_path):
#         print('파일: ', file_path)
#         if target_file in file:
#             check = input('삭제할 파일이 맞나요? (y/n)')
#             if check == 'y':
#                 os.remove(file_path)
#                 print("=" * 100)
#                 print(file_path, "file삭제함")
#                 print("=" * 100)
#             if check == 'n':
#                 break
#     if os.path.isdir(file_path):
#         if target_file in file:
#             check = input('삭제할 폴더가 맞나요? (y/n)')
#             if check == 'y':
#                 os.remove(file_path)
#                 print("=" * 100)
#                 print(file_path, "dir삭제함")
#                 print("=" * 100)
#             if check == 'n':
#                 break

