'''
Created on 2020. 8. 6.

@author: GDJ24
리스트 문제
aa,bb 배열 생성,
aa 배열은 0부터 짝수 20개 저장
bb 배열은 aa 배열의 역순 값 저장
aa,bb 배열 값 출력
'''

aa = []
bb = []
value = 0
for i in range(0,20):
    aa.append(value)
    value += 2
for i in range(0,len(aa)):
    bb.append(aa[len(aa)-1-i])
print(aa)
print(bb)
