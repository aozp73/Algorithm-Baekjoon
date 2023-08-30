import itertools
import math

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    check_nums = nums[1:]  

    # 가능한 모든 쌍에 대해 GCD를 계산하고 합산
    res = 0
    for a, b in itertools.combinations(check_nums, 2):
        res += math.gcd(a, b)

    print(res)




