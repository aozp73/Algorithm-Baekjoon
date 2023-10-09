import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 연결된 육지들에 대해 같은 숫자로 마킹
def bfs1(x, y, count):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    arr[x][y] = count

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                arr[nx][ny] = count
                q.append((nx, ny))

# 각 섬에서 시작, 바다를 건너 다른 섬까지 거리 측정
def bfs2(count):
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == count:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵 벗어날 경우, 탐색 제외
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 다른 섬을 만날 경우, 거리 return
            if arr[nx][ny] > 0 and arr[nx][ny] != count:
                return dist[x][y]
            # 바다나 같은 육지의 경우, 거리 증가
            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                
    return 1e9


# main
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

count = 1
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            bfs1(i, j, count)
            count += 1

answer = min(bfs2(i) for i in range(1, count))
print(answer)
