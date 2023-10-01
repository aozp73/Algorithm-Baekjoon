def tsp_dfs(start, current, total_cost, visited_count):
    global min_cost
    
    # 모든 도시를 방문했을 경우 시작점으로 돌아가는 비용을 확인하고 반환
    if visited_count == N:
        if cities[current][start]:
            total_cost += cities[current][start]
            min_cost = min(min_cost, total_cost)
        return

    # 현재 비용이 이미 찾은 최소 비용보다 큰 경우는 더 이상 탐색하지 않음
    if total_cost >= min_cost:
        return

    for next_city in range(N):
        if not visited[next_city] and cities[current][next_city]:
            visited[next_city] = True
            tsp_dfs(start, next_city, total_cost + cities[current][next_city], visited_count + 1)
            visited[next_city] = False


N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf')
visited = [False] * N

# 각 도시에서 시작하는 경로를 탐색
for start_city in range(N):
    visited[start_city] = True
    tsp_dfs(start_city, start_city, 0, 1)
    visited[start_city] = False

print(min_cost)