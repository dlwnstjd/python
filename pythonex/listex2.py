'''
Created on 2020. 8. 6.

@author: GDJ24
리스트의 기본함수
'''

mylist = [30,10,20]
print("리스트: %s" % mylist)
mylist.append(40)
print("mylist.append(40) 후 리스트: %s" % mylist)
print("pop() 메서드 결과: %s" % mylist.pop())
print("mylist.pop() 후 리스트: %s" % mylist)
mylist.sort()
print("mylist.sort() 후 리트스: %s" % mylist)
mylist.reverse()
print("mylist.reverse() 후 리스트: %s" % mylist)

print("20값의 위치: %d" % mylist.index(20))
mylist.insert(2, 222)   #[30,20,222,10]
print("mylist.insert(2,222) 후 리스트: %s" % mylist)
mylist.remove(222)
print("mylist.remove(222) 후 리스트: %s" % mylist)

mylist.extend([77,77,99])   #다른 리스트 추가
print("mylist.extend([77,77,99]) 후 리스트: %s" % mylist)
print("77값의 갯수: %d" % mylist.count(77))