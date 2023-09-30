from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

max_value = -1e9

for perm in permutations(nums):
    temp = sum(abs(perm[i] - perm[i+1]) for i in range(N-1))
    max_value = max(max_value, temp)

print(max_value)
