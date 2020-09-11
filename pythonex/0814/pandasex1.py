'''
Created on 2020. 8. 14.

@author: GDJ24
pandas 예제
'''

import pandas as pd 
df = pd.DataFrame({"A":[1,4,7],"B":[2,5,8],"C":[3,6,9]})
print(type(df))
print(df)
'''
    행선택
    iloc: 순서, 인덱스기준
    loc: 이름 기준
'''

print("인덱스 값 조회하기")
print("iloc[0]=",df.iloc[0])
print("iloc[1]=",df.iloc[1])
print("loc[0]=",df.loc[0])
#print(df.ix[0]) #버전 2와3 버전의 초기 사용 명령어

#열선택
print("A 열=")
print(df["A"])

df = pd.DataFrame(data=([[1,2,3],[4,5,6],[7,8,9]]),
                  index=[2,"A",4],columns=[51,52,54])
print(df)
print("df.iloc[2]=>")
print(df.iloc[2])
print("df.loc[2]=>")
print(df.loc[2])