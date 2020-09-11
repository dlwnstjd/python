'''
Created on 2020. 8. 14.

@author: GDJ24

0814/pandasex3.py
'''

import pandas as pd

infile="supplier_data.csv"
outfile ="pandas_out3.csv"
#read.csv : csv 파일을 DataFrame 객체로 리턴
df=pd.read_csv(infile)
print(df)

importDate =["1/20/14","1/30/14"]
'''
 부분DataFrame 객체 생성
 Purchase Date 열의 값 중 importDate 속한 모든 컬럼 조회
'''


df_inset = df.loc[df["Purchase Date"].isin(importDate),:]
print(df_inset)
print(type(df_inset))
# to_csv : DataFrame 객체를 csv 파일로 출력.
# index=False :
df_inset.to_csv(outfile,index=False)