'''
Created on 2020. 8. 6.

@author: GDJ24
삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램 작성
삼각형의 높이를 입력하세요: 3
*
**
***
'''

row = int(input("삼각형의 높이를 입력하세요:"))
for i in range(1,row+1):
    print("*" * i)
print()
for i in range(row,0,-1):
    print("*" * i)
print()
for i in range(1,row+1):
    print(" " * (row-i), end="")
    print("*" * i)
print()
for i in range(row,0,-1):
    print(" " * (row-i), end="")
    print("*" * i)
print()
for i in range(1,row+1):
    print(" " * (row-i), end="")
    print("*" * (i*2-1))
print()
for i in range(row,0,-1):
    print(" " * (row-i), end="")
    print("*" * (i*2-1))