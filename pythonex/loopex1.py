'''
Created on 2020. 8. 5.

@author: GDJ24
반복문 연습
'''
num = 0
while num <5:
    print(num,end=",")
    num += 1
print("\nfor구문")
for i in range(0,5):
    print(i,end=",")
    
#1부터 100까지의 합 구하기
sum = 0
for i in range(1,101):
    sum += i
print("\n1부터 100까지의 합:",sum)

#1부터 100까지의 짝수 합 구하기
sum = 0
for i in range(1,101):
    if(i%2==0):
        sum += i
print("\n1부터 100까지의 짝수합:",sum)

#1부터 100까지의 홀수 합 구하기
sum = 0
for i in range(1,101):
    if(i%2==1):
        sum += i
print("\n1부터 100까지의 홀수합:",sum)