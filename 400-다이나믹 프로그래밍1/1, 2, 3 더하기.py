t = int(input())

for _ in range(t):
    n = int(input().rstrip()) 

    dp = [0] * (n + 1)
    
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2  # 1+1, 2
    if n >= 3:
        dp[3] = 4  # 1+1+1, 1+2, 2+1, 3
    
    for i in range(4, n+1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    print(dp[n])