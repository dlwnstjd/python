'''
Created on 2020. 8. 10.

@author: GDJ24
람다를 이용하여 map 처리하기
'''

mylist = [1,2,3,4,5]
#map을 이용하여 mylist 각각의 값에 10 더하기
add = lambda num:num+10
mylist = list(map(add,mylist))
print(mylist)

mylist = list(map(lambda num:num-10,mylist))
mylist = list(map(lambda num:num*10,mylist))
print(mylist)

list1 = [1,2,3,4]
list2 = [10,20,30,40]
hap = lambda n1,n2:n1+n2
haplist = list(map(hap,list1,list2))
print(haplist)
haplist = list(map(lambda n1,n2,n3:n1+n2+n3,mylist,list1,list2))
print(haplist)
print(mylist)