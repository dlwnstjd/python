'''
Created on 2020. 8. 18.

@author: GDJ24
0818/excelex4.py : xls 파일을 읽고 쓰기
'''
from xlrd import open_workbook
from xlwt import Workbook #pip install xlwt

infile ="ssec1804.xls"
outfile = "ssec1804out.xls" # 출력될 xls 파일

outworkbook= Workbook()
out_sheet = outworkbook.add_sheet("전체증감") #sheet 추가

#workbook : infile의 내용 저장 xls 파일 전체
with open_workbook(infile) as workbook :
    #worksheet : sheet 이름이 "1.전체증감" 인 데이터 저장
    worksheet = workbook.sheet_by_name("1.전체증감")
    for rindex in range(worksheet.nrows):
        for cindex in range(worksheet.ncols):
            #out_sheet.write(row인덱스,col 인덱스,값)
            out_sheet.write(rindex,cindex,
            worksheet.cell_value(rindex,cindex))
            print(worksheet.cell_value(rindex,cindex))
outworkbook.save(outfile)  #xls 파일을 file로 저장          