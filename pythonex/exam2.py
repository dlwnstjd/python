'''
Created on 2020. 8. 5.

@author: GDJ24
exam2.py: 초를 입력받아 몇시간 몇분 몇초인지 출력
'''

second = int(input("초를 입력하세요: "))
print(second//3600,"시 ",second%3600//60,"분 ",second%3600%60,"초")
