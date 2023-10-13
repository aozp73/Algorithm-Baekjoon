from collections import deque

def bfs(M, N):
    dist = [[-1] * N for _ in range(M)]  # 벽을 깬 횟수 저장
    dx = [1, 0, -1, 0]  
    dy = [0, 1, 0, -1]  

    queue = deque()
    queue.append((0, 0))  # 시작점
    dist[0][0] = 0  # 시작점의 벽을 깬 횟수: 0
    
    while queue:
        x, y = queue.popleft() 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]  
            
            # 범위 벗어나는 경우 무시
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            # 아직 방문하지 않았다면
            if dist[nx][ny] == -1:
                # 벽이 없는 경우
                if maze[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]  # 이전까지의 벽 부순 횟수 저장
                    queue.appendleft((nx, ny))  # 벽이 없는 경우 우선적으로 탐색
                # 벽이 있는 경우
                else:
                    dist[nx][ny] = dist[x][y] + 1  # 벽 부순 횟수 +1 저장
                    queue.append((nx, ny))  # 벽이 있으므로 나중에 탐색
    return dist[M-1][N-1]

# main
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(M)]

print(bfs(M, N))
