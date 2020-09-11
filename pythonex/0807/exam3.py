'''
Created on 2020. 8. 7.

@author: GDJ24
간단한 계산기 함수
'''

def calc(num1,num2,op):
    sum = 0
    if op == '+':
        sum = num1 + num2
    elif op == '-':
        sum = num1 - num2
    elif op == '*':
        sum = num1 * num2
    else:
        sum = num1 / num2
    return sum
while True:
    oper = input("연산자를 선택하세요:(+,-,*,/) =>")
    var1 = int(input("첫번째 수=>"))
    var2 = int(input("두번째 수=>"))
    res = calc(var1,var2,oper)
    print("계산: %d %s %d = %d" % (var1,oper,var2,res))


