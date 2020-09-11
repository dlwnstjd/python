'''
Created on 2020. 8. 10.

@author: GDJ24
1. 리턴값을 두개이상 반환 => 리스트로 반환
2. 가변매개변수 함수 
'''

def multi(v1,v2):
    list = []
    res1 = v1 + v2
    res2 = v1 - v2
    list.append(res1)
    list.append(res2)
    return list

def multiParam(* p):
    result = 0
    for i in p:
        result += i
        print(i)
        print(p)
    return result

#list=[]
hap,sub=0,0
list = multi(100,200)
#multi(100,200)
hap = list[0]
sub = list[1]
print("multi 함수의 리턴: %d, %d" % (hap,sub))
print("multiParam()=",multiParam())
print("multiParam(10)=",multiParam(10))
print("multiParam(10,20)=",multiParam(10,20))
print("multiParam(10,20,30)=",multiParam(10,20,30))