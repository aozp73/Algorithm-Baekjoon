import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, visited, graph):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, graph)

N, M = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
connected_components = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, visited, graph)
        connected_components += 1

print(connected_components)