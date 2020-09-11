'''
Created on 2020. 8. 12.

@author: GDJ24
sqlite db 사용하기
'''

import sqlite3  #sqlite db 모듈
dbpath = "text.sqlite"
conn = sqlite3.connect(dbpath)  #test.sqlite db에 접속
cur = conn.cursor() #명령 전달 객체
#여러 문장을 실행 가능.
cur.executescript('''
    drop table if exists items;
    create table items (item_id integer primary key,
    name text unique,
    price integer);
    insert into items (name, price) values ('Apple',800);
    insert into items (name, price) values ('Orange',500);
    insert into items (name, price) values ('Banana',300);
''')
conn.commit()   #Transaction완료. 정상처리. rollback(): 취소 완료
cur=conn.cursor()
cur.execute("select * from items")
item_list = cur.fetchall()  #전체조회
print(type(item_list))  #list
for it in item_list:
    print(type(it))
    print(it)