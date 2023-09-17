N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# 초기 DP 테이블 생성
dp = [[0] * 3 for _ in range(N)]

# 첫 번째 집을 각각 R, G, B로 칠할 경우에 대해 각각 DP 수행
result = 1e9  # 최솟값을 저장할 변수

for first in range(3):
    for i in range(3):
        if i == first:
            dp[0][i] = costs[0][i]
        else:
            dp[0][i] = 1e9  # 첫 번째 집의 색이 정해져 있으므로 나머지 색은 사용 불가능하게 설정
    
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    for last in range(3):
        if last == first:
            continue  # 첫 번째 집과 마지막 집의 색은 같을 수 없으므로 건너뜀
        result = min(result, dp[-1][last])  # 최솟값 업데이트

print(result)