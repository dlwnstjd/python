'''
Created on 2020. 8. 13.

@author: GDJ24
파일에 내용 쓰기
'''

outfp = None
outfp = open("data.txt","w",encoding="UTF8")
while True:
    outstr = input("내용 입력:")    #화면에서 내용입력
    if outstr != "":
        outfp.writelines(outstr + "\n") #한줄을 파일에 저장
    else:
        break
outfp.close()
print("프로그램 종료")
