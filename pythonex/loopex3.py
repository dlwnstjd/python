'''
Created on 2020. 8. 6.

@author: GDJ24
랜덤 함수를 사용하여 숫자 맞추기
1. 1부터 99까지의 임의의 수를 저장,
2. 화면에 숫자 입력
3. 입력된 수가 저장된 수보다 크면 작으수를 입력하세요 메세지 출력
     입력된 수가 저장된 수보다 작으면 더 큰수를 입력하세요 메세지 출력
4. 저장된 수와 입력된 수가 같은 경우, 입력 건수를 화면에 출력하고 프로그램 종료
'''
import random
rnum = random.randrange(1,100)
i = 0
#True: 예약어. while 구문은 무한 반복.
while True:
    a = int(input("숫자를 입력하세요: "))
    if a > rnum:
        print("작은 수 입니다.")
    elif a < rnum:
        print("큰 수 입니다.")
    else:
        print("정답입니다.")
        break
    i += 1
#정답을 맞춘 경우 실행. while 구문의 바깥문장
print("%d번 만에 맞췄습니다." % i)