'''
Created on 2020. 8. 13.

@author: GDJ24
regularex3.py 파일을 읽어서
regularex3.bak 파일로 복사
'''

infp,outfp = None,None
inStr = ""
infp = open("regularex3.py","r", encoding="UTF8")
outfp = open("regularex3.bak","w",encoding="UTF8")
while True:
    inStr = infp.readline() 
    if not inStr:   #EOF(End of File)
        break
    outfp.writelines(inStr)
outfp.close()
infp.close()
print("프로그램 종료")