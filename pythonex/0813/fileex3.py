'''
Created on 2020. 8. 13.

@author: GDJ24
파일의 정보 조회하기
'''

import os.path

file="fileex1.py"
file="../0813"
file="C:\\ui\\python\\pythonex\\0813"
if os.path.isfile(file):
    print(file, "은 파일 입니다.")
elif os.path.isdir(file):
    print(file, "은 폴더 입니다.")

if os.path.exists(file):
    print(file, "은 존재합니다.")
else:
    print(file, "은 없는 파일입니다.")