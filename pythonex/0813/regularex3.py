'''
Created on 2020. 8. 13.

@author: GDJ24
정규식 예제
'''
import re

str = "The quick brown fox jumps over the lazy dog Te Thhe Thhhe."
str_list = str.split()
pattern = re.compile("Th?e")    #T자로 시작하고, h문자가 1개이상이면서 e문자로 종료하는 문자
count = 0
for word in str_list:
    if pattern.search(word):    #pattern에 맞는 문자?
        count += 1
print("output 1: {1:s}:{0:d} ".format(count, "갯수"))

#re.I: 대소문자 구분 없이.
pattern = re.compile("Th*e",re.I)   
count = 0
for word in str_list:
    if pattern.search(word):    #pattern에 맞는 문자?
        count += 1
print("output 2: {1:s}:{0:d} ".format(count, "갯수"))

pattern = re.compile("(?P<match_word>Th*e)",re.I)   
print("output3:",end=" ")
count = 0
for word in str_list:
    if pattern.search(word):    #pattern에 맞는 문자?
        print("{0}".format(pattern.search(word).group("match_word")),end=",")
print()
#pattern.sub: pattern에 맞는 문자열을 지정한 문자로 치환
str_find = "The"
pattern = re.compile(str_find,re.I)
print("output4: {0}".format(pattern.sub("a",str)))





