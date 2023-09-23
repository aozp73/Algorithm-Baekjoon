from itertools import permutations

N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

for p in permutations(li, M):
    print(' '.join(map(str, p)))