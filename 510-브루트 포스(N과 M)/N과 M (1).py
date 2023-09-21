from itertools import permutations

n, m = map(int, input().split())

li = [num for num in range(1, n+1)]

for p in permutations(li, m):
    print(' '.join(map(str, p)))