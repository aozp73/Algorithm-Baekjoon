from itertools import product

N, M = map(int, input().split())
nums = sorted(set(map(int, input().split()))) 

res = list(product(nums, repeat=M)) 

for r in res:
    print(' '.join(map(str, r)))