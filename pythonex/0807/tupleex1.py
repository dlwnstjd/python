'''
Created on 2020. 8. 7.

@author: GDJ24
튜플예제: 변경불가 리스트
'''

tp1 = (10,20,30)
print(tp1)
print(tp1[0],tp1[1],tp1[2])
#tp1.append(100) => 변경 불가
#tp1[0] = 100 => 변경 불가
#리스트로 변경후 수정
list = list(tp1)    #리스트 <= 튜플
list.append(40)     #요소 추가
list[0]=100         #요소 수정
print(list)
tp1 = tuple(list)
print(tp1)
print("tp1의 크기:",len(tp1),", list의 크기:", len(list))
print("tp1[1:3]의 크기:",tp1[1:3],", list[1:3]:", list[1:3])
print("tp1[:3]의 크기:",tp1[:3],", list[:3]:", list[:3])
print("tp1[2:]의 크기:",tp1[2:],", list[2:]:", list[2:])
print("tp1[::2]의 크기:",tp1[::2],", list[::2]:", list[::2])
