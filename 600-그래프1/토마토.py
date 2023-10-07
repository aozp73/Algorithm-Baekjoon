from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

# 초기에 익은 토마토 위치를 모두 큐에 추가
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))
bfs()


# 모든 토마토가 익었는지 확인하고, 최대 값 구하기
days = -1
for i in tomato:
    for j in i:
        if j == 0:  # 아직 익지 않은 토마토가 존재하는 경우
            print(-1)
            exit(0)
        days = max(days, j)

if days == 1:
    print(0)
else:
    print(days - 1)