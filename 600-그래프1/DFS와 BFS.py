from collections import deque

def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        v = queue.popleft()
        result.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return result

def dfs(graph, v, visited=None):
    if visited is None:
        visited = [False] * (len(graph))
    visited[v] = True
    result = [v]

    for i in graph[v]:
        if not visited[i]:
            result += dfs(graph, i, visited)

    return result

# 입력 값
N, M, V = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 인접 행렬 2차원 리스트에 저장
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)

# 간선 정보에 따라 오름차순으로 정렬
for i in range(1, N+1):
    graph[i].sort()

print(*dfs(graph, V))
print(*bfs(graph, V))
