T = int(input())

for _ in range(T):
    n = int(input())
    
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))

    dp = [[0] * n for _ in range(2)]

    dp[0][0] = row1[0]
    dp[1][0] = row2[0]

    if n > 1:
        dp[0][1] = row2[0] + row1[1]
        dp[1][1] = row1[0] + row2[1]
        
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + row1[i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + row2[i]
    
    print(max(dp[0][-1], dp[1][-1]))