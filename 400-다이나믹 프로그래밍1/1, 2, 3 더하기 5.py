import sys

input = sys.stdin.readline

dp = [[0 for _ in range(3)] for _ in range(100001)]

# 계산식이 1, 2, 3으로 끝나는 경우의 수 기입
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    
    # i-1에서 2로 끝나는 경우, 3으로 끝나는 경우에서 각각 + 1
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    # i-2에서 1로 끝나는 경우, 3으로 끝나는 경우에서 각각 + 2
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    # i-3에서 1로 끝나는 경우, 2로 끝나는 경우에서 각각 + 3
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009

T = int(input())
for i in range(T):
    n = int(input())
    print(sum(dp[n]) % 1000000009)