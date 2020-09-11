'''
Created on 2020. 8. 19.

@author: GDJ24
'''

import pandas as pd
import glob
import os

inpath="C:/ui/python/pythonex/excel/"
outfile = "sales_all.xlsx"
excels = glob.glob(os.path.join(inpath,"*.xlsx"))
rows = []
for excel in excels:
    print(excel)
    dfs = pd.read_excel(excel,sheet_name=None,index_col=None)
    for sheet_name,df in dfs.items():
        rows.append(df)
df_concat = pd.concat(rows,sort=False,axis=0,ignore_index=True)
writer = pd.ExcelWriter(outfile)
df_concat.to_excel(writer,sheet_name="al_data_all_worksheet",index=False)
writer.save()
