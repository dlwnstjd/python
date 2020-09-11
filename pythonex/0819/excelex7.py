'''
Created on 2020. 8. 19.

@author: GDJ24
'''

import pandas as pd

infile = "../0818/ssec1804.xlsx"
outfile = "ssec1804_bak.xlsx"
writer = pd.ExcelWriter(outfile)
df = pd.read_excel(infile,sheet_name=None,index_col=None)
for worksheet_name,data in df.items():
    print("===",worksheet_name,"===")
    print(data)
    data.to_excel(writer,sheet_name=worksheet_name,index=False,header=False)
writer.save()
