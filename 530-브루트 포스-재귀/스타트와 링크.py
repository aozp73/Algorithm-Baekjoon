from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 모든 가능한 팀의 조합 생성
teams = list(combinations(range(N), N//2))
min_diff = float('inf')

# 전체 팀 조합의 절반만 확인
for i in range(len(teams)//2): 
    start_team = teams[i]
    link_team = teams[-i-1]
    
    start_stat = 0
    for x in start_team:
        for y in start_team:
            start_stat += S[x][y]

    link_stat = 0
    for x in link_team:
        for y in link_team:
            link_stat += S[x][y]

    # 두 팀의 능력치 차이 계산
    diff = abs(start_stat - link_stat)

    # 최소 능력치 차이 업데이트
    min_diff = min(min_diff, diff)

print(min_diff)
