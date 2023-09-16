N = int(input())
dp = [0] * (N + 1)

if N % 2 == 1:
    print(0)
else:
    dp[0] = 1  # 3x0 벽: 이미 채워져 있는 경우 1가지
    dp[2] = 3  # 3x2 벽: 3가지 경우로 채울 수 있음

    for i in range(4, N + 1, 2):
        dp[i] = dp[i-2] * 3  # 기본적인 3가지 경우

        # 나머지 경우 추가 (앞의 두칸이 dp[i-2]이므로, 2칸씩 줄여가면서 고려)
        for j in range(4, i + 1, 2):
            dp[i] += dp[i-j] * 2  # 각각의 경우는 2가지 방법으로 채울 수 있음

    print(dp[N])