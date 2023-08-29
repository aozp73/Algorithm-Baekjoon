# 팩토리얼 함수
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n -1)

# 스크립트 시작점
n = input().rstrip()
str_n = str(factorial(int(n)))
cnt = 0

for num in str_n[::-1]:
    if num == '0':
        cnt += 1
    else:
        break
    
print(cnt)