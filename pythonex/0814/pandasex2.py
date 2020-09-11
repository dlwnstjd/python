'''
Created on 2020. 8. 14.

@author: GDJ24
pandas를 이용하여 csv 파일 읽기
'''

import pandas as pd

infile = "서울특별시_구로구_CCTV_20200427_1587989291679_248451.csv"
outfile = "pandas_out2.csv"
df = pd.read_csv(infile)
print(df)