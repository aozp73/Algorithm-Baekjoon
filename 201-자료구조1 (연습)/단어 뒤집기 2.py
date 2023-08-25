s = input()
tag = False
word = ''

for char in s:
    # 태그 처리 ~
    if char == '<':    # 태그 시작
        if word:  
            print(word[::-1], end='')
            word = ''
        tag = True
        print('<', end='')
    elif char == '>':  # 태그 끝
        tag = False
        print('>', end='')
    elif tag:          # 태그 내부 문자
        print(char, end='')
    # ~ 태그 처리
    
    elif char == ' ': 
        print(word[::-1], end=' ')
        word = ''
    else: 
        word += char

# 공백 이 후, 마지막 문자 처리 용도
if word: 
    print(word[::-1])