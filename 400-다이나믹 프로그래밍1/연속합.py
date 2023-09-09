n = int(input())
arr = list(map(int, input().split()))

# dp[i] : i번째 수를 마지막으로 가지는 연속된 수의 최대 합
dp = [0] * n
dp[0] = arr[0] 

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])  

print(max(dp))  