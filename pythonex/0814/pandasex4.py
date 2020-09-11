'''
Created on 2020. 8. 14.

@author: GDJ24
pandas 부분선택예제
'''

import pandas as pd

infile = "supplier_data.csv"
outfile = "pandas_out4.csv"

df = pd.read_csv(infile)
df_inset = df.loc[df["Invoice Number"].str.startswith("920-")]
print(df_inset)
df_inset.to_csv(outfile,index=False)