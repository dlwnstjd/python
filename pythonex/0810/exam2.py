'''
Created on 2020. 8. 10.

@author: GDJ24
문자열 문제
'''
from test.test_buffer import rpermutation

ss = "홍길동"  
# 홍#길#동# 출력
# print(ss[0],end="#")
# print(ss[1],end="#")
# print(ss[2],end="#")
for i in range(len(ss)):
    print(ss[i],end="#")
print()
#동길홍 출력
for i in range(len(ss)-1,-1,-1):
    print(ss[i],end="")
print()
print(ss[::-1])