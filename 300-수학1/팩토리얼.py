# 1. 재귀함수
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))


# 2. 반복문
n = int(input())
result = 1

for i in range(1, n + 1):
    result *= i

print(result)