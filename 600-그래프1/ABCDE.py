n, m = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, depth):
    if depth == 4:
        return True
    for friend in graph[node]:
        if not visited[friend]:
            visited[friend] = True
            if dfs(friend, depth + 1):  
                return True
            visited[friend] = False
    return False

# 각 노드마다 DFS 수행
for i in range(n):
    visited = [False] * n 
    visited[i] = True  
    if dfs(i, 0):  
        print(1)
        break
else:  
    print(0)
