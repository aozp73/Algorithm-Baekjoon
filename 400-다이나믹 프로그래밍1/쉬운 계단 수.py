N = int(input())  # 자리수 입력

# DP 배열 초기화. dp[i][j]는 길이가 i이고 마지막 숫자가 j인 계단 수의 개수
dp = [[0] * 10 for _ in range(N + 1)]

# 길이가 1인 계단 수 초기화
for i in range(1, 10): 
    dp[1][i] = 1

# 길이가 i이고, 마지막 숫자가 j인 계단 수의 개수 구하기
for i in range(2, N + 1):
    for j in range(10):
        if j == 0:   # 현재 마지막 자리수가 0일 경우, 이전 자리에 1만 올 수 있음
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9: # 마지막 자리수가 9라면, 이전 자리에 8만 올 수 있음
            dp[i][j] = dp[i - 1][j - 1]
        else: # 마지막 자리수가 1 ~ 8이라면, 이전 자리에 2가지가 올 수 있음
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            
        dp[i][j] %= 1000000000

print(sum(dp[N]) % 1000000000)
