'''
Created on 2020. 8. 7.

@author: GDJ24
배열의 값의 합과 평균을 구하는 함수 작성
'''

def getSum(numlist):
#     sum = 0
#     for i in range(0,len(numlist)):
#         sum += numlist[i]
    return sum(numlist)
def getMean(numlist):
#     sum = 0
#     for i in range(0,len(numlist)):
#         sum += numlist[i]
#         sum = sum / len(numlist)
#     if len(numlist) > 0 :
#         return sum(numlist)/len(numlist) 
#     else:
#         return 0
#    return sum(numlist)/len(numlist)  if len(numlist) > 0 else 0
    #\밑에줄도 한문장이라고 알려줌
    return sum(numlist)/len(numlist)\
        if len(numlist) > 0 else 0

list = [2,3,3,4,4,5,5,6,6,8,8]
print("list의 값의 합:", getSum(list))
print("list의 값의 평균:", getMean(list))

list2 = []
print("list2의 값의 합:", getSum(list2))
print("list2의 값의 평균:", getMean(list2))

tp = [2,3,3,4,4,5,5,6,6,8,8]
print("list의 값의 합:", getSum(tp))
print("list의 값의 평균:", getMean(tp))

num = 10
print(type(num))
num = 10.5
print(type(num))







