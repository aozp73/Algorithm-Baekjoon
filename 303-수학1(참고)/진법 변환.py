n, b = input().split()
b = int(b)

result = 0
length = len(n)

for i in range(length):
    x = n[i]
    
    # x가 숫자인지, 알파벳 대문자인지 확인
    if '0' <= x <= '9':
        x = int(x)
    else:
        x = ord(x) - ord('A') + 10
    
    # 현재 자릿수에 해당하는 B의 거듭제곱을 곱하고 결과에 더함
    result += x * (b ** (length - i - 1))

print(result)