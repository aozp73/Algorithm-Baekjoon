from collections import deque

def bfs(N, K):
    # 방문 여부 및 시간을 저장할 리스트, 최대 범위인 100001로 초기화
    visited = [-1] * 100001
    visited[N] = 0
    queue = deque([N])

    while queue:
        current = queue.popleft()
        if current == K:
            return visited[current]
        
        # 순간이동
        if 0 <= 2 * current <= 100000 and visited[2 * current] == -1:
            visited[2 * current] = visited[current]
            queue.appendleft(2 * current)
        
        # 걷기 (뒤로)
        if 0 <= current - 1 and visited[current-1] == -1:
            visited[current-1] = visited[current] + 1
            queue.append(current-1)
        
        # 걷기 (앞으로)
        if current+1 <= 100000 and visited[current+1] == -1:
            visited[current+1] = visited[current] + 1
            queue.append(current+1)

N, K = map(int, input().split())
print(bfs(N, K))