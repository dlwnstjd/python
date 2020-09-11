'''
Created on 2020. 8. 19.

@author: GDJ24
sales_2013.xlsx 파일 중
Purchase Date 컬럼의 값이 "01/24/2031"과
"01/31/2013" 인 행만 sales_2013_01.xlsx 파일로 저장
'''

import pandas as pd

infile = "../0818/sales_2013.xlsx"
outfile = "sales_2013_01.xlsx"
df = pd.read_excel(infile,"january_2013",index_col=None)
select_date = ['01/24/2013','01/31/2013']
df_value = df[df['Purchase Date'].isin(select_date)]
print(df_value)
writer = pd.ExcelWriter(outfile,engine="openpyxl")
df_value.to_excel(writer,sheet_name="jan_13_output",index=False)
writer.save()