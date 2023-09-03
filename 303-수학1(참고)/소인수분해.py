n = int(input())

# 소인수분해 함수
def prime_decomposition(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            print(i)
            n //= i
        i += 1
    if n > 1:
        print(n)

prime_decomposition(n)