'''
Created on 2020. 8. 18.

@author: GDJ24
0818/excelex3.py : xls 파일 읽기
'''

from xlrd import open_workbook
infile = "ssec1804.xls"
workbook=open_workbook(infile)
print("sheet 의 갯수:",workbook.nsheets)
for worksheet in workbook.sheets():
    print("worksheet 이름:",worksheet.name)
    print("행의 수",worksheet.nrows)
    print("컬럼의 수",worksheet.ncols)
    #내용 출력
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            print(worksheet.cell_value(
                row_index,column_index),",",end="")
        print()    
