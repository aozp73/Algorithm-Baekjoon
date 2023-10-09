from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(v, prev):
    
    # 순환선 발견 조건 : 방문했던 노드 재방문
    if visited[v] != -1:
        while prev != v:
            # 순환선에 속하는 노드를 cycle 리스트에 저장
            cycle.append(prev)
            prev = visited[prev]
        cycle.append(v)
        return True
    
    visited[v] = prev
    for next_v in graph[v]:
        if next_v == prev: continue
        if dfs(next_v, v): return True
        
    return False


# main
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (n+1)
cycle = []

# 순환선 찾기 (DFS)
dfs(1, 0)

# 순환선 까지의 거리 계산 (BFS)
dist = [-1] * (n + 1)
q = deque(cycle)
for c in cycle:
    dist[c] = 0

while q:
    v = q.popleft()
    for nv in graph[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            q.append(nv)

# 문제 조건의 포멧으로 출력
print(' '.join(map(str, dist[1:])))