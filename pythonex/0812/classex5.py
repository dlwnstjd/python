'''
Created on 2020. 8. 12.

@author: GDJ24
추상메서드 예제
=>자손 클래스에서 반드시 오버라이딩 필요
'''
class SuperClass:
    def method(self):   #추상메서드
        raise NotImplementedError   #자손클래스에서 오보라이딩 해야 함

class SubClass1(SuperClass):
    def method(self):
        print("SubClass1에서 method()를 오버라이딩 함")
        
class SubClass2(SuperClass):
    def method(self):
        print("SubClass2에서 method()를 오버라이딩 함")

su = SuperClass()
print(su)
su.method()
sub1 = SubClass1()
sub2 = SubClass2()
sub1.method()
sub2.method()