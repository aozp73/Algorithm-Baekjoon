N = int(input())

A = list(map(int, input().split()))

# dp[i]: i번째 원소를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
dp = [1] * N

# LIS 알고리즘
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))