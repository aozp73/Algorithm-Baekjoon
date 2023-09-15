N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))