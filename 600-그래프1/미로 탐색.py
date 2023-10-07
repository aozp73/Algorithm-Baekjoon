from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 미로 공간을 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 
            if maps[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    return maps[n-1][m-1]

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().strip())))

print(bfs(0, 0))