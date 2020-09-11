'''
Created on 2020. 8. 19.

@author: GDJ24
'''

import pandas as pd

infile = "../0818/sales_2013.xlsx"
outfile = "sales_2013_allamt.xlsx"
writer = pd.ExcelWriter(outfile)
df = pd.read_excel(infile,sheet_name=None,index_col=None)
for worksheet_name,data in df.items():
    print("===",worksheet_name,"===")
    data_value = data.loc[:,["Customer Name","Sale Amount"]]
    data.to_excel(writer,sheet_name=worksheet_name,index=False)
writer.save()
