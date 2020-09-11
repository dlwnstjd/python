'''
Created on 2020. 8. 7.

@author: GDJ24
나라와 수도를 등록하고 화면에 나라이름을 입력받아 해당 나라의 수도 출력
등롣된 나라가 아닌경우 수도를 입력받아 등록
종료시 등록된 모든 나라와 수도정보를 화면 출력
'''

country = {"대한민국":"서울","일본":"도쿄","독일":"베를린","뉴질랜드":"웰링턴","러시아":"모스크바"}

while True :
    indata = input(str(list(country.keys()))+"수도를 알고 싶은 나라는?")
    if indata in country :
        print("<%s> 나라의 수도는 <%s>입니다."
                            %(indata,country.get(indata)))
    elif indata=="종료":
        for i in country.keys():
            print("%s => %s " % (i,country[i]))
        break
    else:
        print("등록된 나라가 아닙니다.")
        yn = input("수도를 등록하시겠습니까?(y/n)")
        if yn =='y':
            f = input("수도이름을 입력하세요")
            country[indata] = f