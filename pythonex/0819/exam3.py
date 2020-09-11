'''
Created on 2020. 8. 19.

@author: GDJ24
'''

import pandas as pd

infile = "../0818/sales_2013.xlsx"
outfile = "sales_2013_amt.xlsx"
df = pd.read_excel(infile,"january_2013",index_col=None)
df_value = df.loc[:,["Customer Name", "Sale Amount"]]
writer = pd.ExcelWriter(outfile)
df_value.to_excel(writer,sheet_name="january_2013",index=False)
writer.save()
