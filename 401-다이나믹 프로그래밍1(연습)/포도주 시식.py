n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]

if n > 2:
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])

for i in range(3, n):
    dp[i] = max(
        dp[i-3] + wine[i-1] + wine[i],  # 현재 포도주와 바로 전 포도주를 마시는 경우
        dp[i-2] + wine[i],  # 현재 포도주만 마시는 경우
        dp[i-1]  # 현재 포도주를 마시지 않는 경우
    )

print(max(dp))