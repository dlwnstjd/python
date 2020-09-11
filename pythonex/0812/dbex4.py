'''
Created on 2020. 8. 12.

@author: GDJ24
mariadb 사용하기
'''

import pymysql  #pip install pymysql 

conn = pymysql.connect(host="localhost",port=3306,
                       user="scott",password="1234",
                       db="classdb",charset="utf8")
try:
    cur = conn.cursor()
    cur.execute("select * from item")
#     for row in cur.fetchall():    #모든 레코드 조회
#         print(row[0],row[1],row[2])
    while True:
        row = cur.fetchone()    #한개의 레코드만 조회
        if row == None: #조회된 레코드가 없음
            break
        print(row)
finally:
    cur.close()
    conn.close()
    