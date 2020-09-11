'''
Created on 2020. 8. 12.

@author: GDJ24
mariadb에 데이터 추가하기
'''

import pymysql
conn = pymysql.connect(host="localhost",port=3306,
                       user="scott",password="1234",
                       db="classdb",charset="utf8")
cur = conn.cursor()
data = [
    (10, "바나나", 3000, "바나나는 길다"),(11, "망고", 3000, "망고는 열대 과일이다."),
    (12, "배", 3000, "배는 우리나가 배가 제일 맛있다.") ]
for i in data:
    cur.execute('''insert into item(id,name,price,description)
    values (%s,%s,%s,%s)''',i)
cur.execute("select * from item")
for row in cur.fetchall():    #모든 레코드 조회
    print(row)
conn.rollback()