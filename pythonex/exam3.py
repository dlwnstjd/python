'''
Created on 2020. 8. 5.

@author: GDJ24
숫자를 입력받아 입력된 값까지의 전체합, 짝수합, 홀수합 구하기
'''

num = int(input("숫자를 입력하세요:"))

sum = 0
for i in range(0,num+1):
    sum += i
print("전체합:",sum)

sum = 0
for i in range(0,num+1):
    if(i%2==0):
        sum += i
print("짝수합:",sum)

sum = 0
for i in range(0,num+1):
    if(i%2==1):
        sum += i
print("홀수합:",sum)