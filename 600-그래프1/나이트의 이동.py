from collections import deque

def bfs(x, y, target_x, target_y, l):
    visited = [[False] * l for _ in range(l)]
    queue = deque([(x, y, 0)])  # 현재 위치, 움직인 횟수
    visited[x][y] = True
    
    while queue:
        x, y, count = queue.popleft()
        
        # 목표 지점에 도달했을 경우 count 반환
        if x == target_x and y == target_y:
            return count
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True
                
    return -1  # 이동할 수 없는 경우


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())

for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    print(bfs(x, y, target_x, target_y, l))