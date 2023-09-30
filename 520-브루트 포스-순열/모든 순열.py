from itertools import permutations

N = int(input())
nums = [num for num in range(1, N + 1)]

for p in(permutations(nums, N)):
    print(' '.join(map(str, p)))