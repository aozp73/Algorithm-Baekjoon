# 에라토스테네스의 체
r = 1000001
check = [True] * r
for i in range(2, int(r ** 0.5) + 1):
    if check[i]:
        for j in range(i + i, r, i):
            check[j] = False

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n, 2):  # 홀수만 검사
        if check[i] and check[n - i]:
            print(f"{n} = {i} + {n - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")