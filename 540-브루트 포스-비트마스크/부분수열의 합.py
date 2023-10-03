from itertools import combinations

N, S = map(int, input().split())
seq = list(map(int, input().split()))

ans = 0

for i in range(1, N+1):
    for subset in combinations(seq, i):
        if sum(subset) == S:
            ans += 1

print(ans)