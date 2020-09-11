'''
Created on 2020. 8. 18.

@author: GDJ24
0818/excelex2.py  :xlsx의 모든 sheet 읽기
'''
import openpyxl
filename="sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
for sheet in book.worksheets :
    data = []
    #sheet.rows : sheet의 행들
    #row : 한줄
    for row in sheet.rows:
        line=[]
        for i,c in enumerate(row):
            line.append(c.value)
        print(line)
        data.append(line)    
