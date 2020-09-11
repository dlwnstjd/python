'''
Created on 2020. 8. 6.

@author: GDJ24
문자열 처리. 문자열을 배열로 처리 가능함.
'''
print("안녕하세요")
print("안녕하세요"[0])
print("안녕하세요"[4])
print("안녕하세요"[-1])
print("안녕하세요"[-4])

#부분문자열
print("안녕하세요"[1:3]) #1번 인덱스부터 2번 인덱스까지 출력
print("안녕하세요"[:3]) #처음부터 2번인덱스까지 부분 문자열
print("안녕하세요"[3:]) #3번 인덱스부터 끝까지
print("안녕하세요"[::2]) #2칸씩 부분문자열
print("안녕하세요"[::-1]) #역순으로 출력
print("안녕하세요"[::-2]) #역순의 2칸간격으로 출력

#함수
print(type("안녕하세요"))    #자료형
print(len("안녕하세요"))     #문자열 길이

a = "hello"
cnt = 0
# l문자의 갯수 출력
for i in range(0,len(a)):
    if(a[i] == 'l'):
        cnt += 1
print("l문자의 갯수:",cnt)
print("l문자의 갯수:",a.count("l"))
print("l문자의 위치:",a.find("l"))
print("a문자의 위치:",a.find("a"))
print("l문자의 위치:",a.index("l"))
print("a문자의 위치:",a.index("a"))



