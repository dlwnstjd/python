'''
Created on 2020. 8. 5.

@author: GDJ24
python.py: 파이썬 예제 1

1. ''' ''' 여러줄 주석
   #       한줄 주석
2. 변수 선언 필요 없음
3. {    } 블럭이 없음
    공백으로 처리함

'''
print("Hello World")

sel = int(input('입력 진수 결정(16/10/8/2): '))
num = input("값 입력: ")
if sel == 16:
    num10 = int(num,16)
    print("16진수",num,":",num10) 
    ''' 
    int() 형변환 연산자
    num,16진수: num을 16진수로 인식하여 정수형 리턴
    '''
if sel == 10:
    num10 = int(num,10)
    print("10진수",num,":",num10)
if sel == 8:
    num10 = int(num,8)
    print("8진수",num,":",num10)
if sel == 2:
    num10 = int(num,2)
    print("2진수",num,":",num10)
print(num10)
print(type(num))

num = num10
print(type(num))
print(type(num10))
#10진수를 2,8,10,16 진수로 변경 출력
print("16진수=>",hex(num10))
print("8진수=>",oct(num10))
print("2진수=>",bin(num10))
