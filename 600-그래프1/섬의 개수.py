import sys
sys.setrecursionlimit(10**6)

# 방향 (상, 하, 좌, 우, 왼쪽 위 대각선, 오른쪽 위 대각선, 왼쪽 아래 대각선, 오른쪽 아래 대각선)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y, w, h, graph):
    graph[x][y] = 0  
    for i in range(8): 
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny, w, h, graph)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j, w, h, graph)
                count += 1
    print(count)
