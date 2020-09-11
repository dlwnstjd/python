'''
Created on 2020. 8. 13.

@author: GDJ24
csv 파일 읽기
command 라인에서 입력 파일을 입력받기
'''

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
with open(infile,"r",newline="",encoding="UTF8") as filereader :
    with open(outfile,"w",newline="") as filewriter :
        header = filereader.readline()
        print(type(header))
        #headlist: list형
        headlist = header.split(",")
        filewriter.write(",".join(map(str,headlist)) + "\r\n")
        for rowlist in filereader:
            filewriter.write(rowlist)