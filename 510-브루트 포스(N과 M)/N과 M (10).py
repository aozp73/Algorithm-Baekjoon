from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

res = sorted(list(set(combinations(nums, M))))

for r in res:
    print(' '.join(map(str, r)))