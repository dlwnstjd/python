'''
Created on 2020. 8. 10.

@author: GDJ24
피보나치 수열 출력하기
피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : 5
[0,1,1,2,3]
피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : 10
[0,1,1,2,3,5,8,13,21,34]
'''

def fibo(n):
    fibolist = []
    num1 = 0
    num2 = 1
    num3 = num1 + num2
    fibolist.append(num1)
    fibolist.append(num2)
    fibolist.append(num3)
    for i in range(3,n):
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        fibolist.append(num3)
    return fibolist

num = int(input("피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) :"))
print("f(",num,")=",end="")
print(fibo(num))