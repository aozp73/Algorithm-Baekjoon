from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

res = sorted(list(set(permutations(nums, M))))

for r in res:
    print(' '.join(map(str, r)))
