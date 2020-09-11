'''
Created on 2020. 8. 12.

@author: GDJ24
정규식 예제
'''

data = '''
    park 800805-1234567
    kim  700905-2345678
    choi 750905-a123456
'''
result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))