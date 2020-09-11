'''
Created on 2020. 8. 12.

@author: GDJ24
정규식 사용하기
    (): 그룹화
    []: 문자부분 설정
    {갯수}: 갯수
    \d: 숫자
    (\d{6,7})[-]\d{7}:
        첫번째 그룹: 숫자가  6자리 또는 7자리그룹
        다음은 문자 -
        다음은 숫자 7자리
    /g<1>: 설정된 첫번째 그룹 의미
    
    ?: 0 또는 1개
        ca?t: a 문자가 없거나 1개인 경우
        "ct": true
        "cat": true
        "caaaaat": false
    *: 0개 이상
        ca*t: a 문자가 0개 이상인 경우
        "ct": true
        "cat": true
        "caaaaat": true
    +: 1개 이상
        ca+t: a 문자가 1개 이상인 경우
        "ct": false
        "cat": true
        "caaaaat": true
    {n}: n개 반복
        ca{2}t: a 문자가 2개 필요
        "ct": false
        "caat": true
        "caaaaat": false
    {n,m}: n개 이상 m개 이하
        ca{2,5}t: a 문자가 2개 이상 5개 이하
        "ct": false
        "cat": false
        "caat": true
        "caaaaat": true
'''

import re

data = '''
    park 800805-1234567
    kim  700905-2345678
    choi 750905-a123456
'''
'''
re.compile(pattern): pattern에 맞는 문자열을 지정
'''
pat = re.compile("(\d{6,7})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))