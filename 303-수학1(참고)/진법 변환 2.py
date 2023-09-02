n, b = map(int, input().split())

result = ''

while n > 0:
    remainder = n % b

    # 나머지가 10 이상인 경우에 알파벳 대문자로 변환
    if remainder >= 10:
        result += chr(ord('A') + remainder - 10)
    else:
        result += str(remainder)
    
    n //= b

print(result[::-1])