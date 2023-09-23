from itertools import combinations

N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

for p in combinations(li, M):
    print(' '.join(map(str, p)))