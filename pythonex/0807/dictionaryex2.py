'''
Created on 2020. 8. 7.

@author: GDJ24
'''
foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","맥주":"치킨"}
for i in foods.keys():  #map.keySet()
    print("%s=>%s" % (i,foods[i]))
    
while True:
    myfood = input(str(list(foods.keys())) + "중 음식이름 입력:")
    if myfood == "종료":
        print("등록된 음식 갯수:" + str(len(foods)))   #키의 갯수
        print("좋아하는 음식:" + str(list(foods.keys())))
        print("궁합음식:" + str(list(foods.values())))  #map.values()
        print(list(foods.items()))
        break
    if myfood in foods: #myfood값이 foods의 key에 존재하냐
        print("<%s> 궁합음식은 <%s>입니다." % (myfood,foods[myfood]))
    else:
        print("등록된 음식이 아닙니다.")
        yn = input("좋아하는 음식으로 등록 하시겠습니까?(Y)")
        if yn == 'Y' or yn == 'y':
            f = input("궁합음식을 입력하세요:")
            foods[myfood] = f