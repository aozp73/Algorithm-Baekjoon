from collections import deque

def bfs(n, k):
    MAX_SIZE = 100001
    visited = [0] * MAX_SIZE

    queue = deque()
    queue.append(n)
    visited[n] = 1

    while queue:
        current = queue.popleft()
        
        # 기저 조건 : 동생의 위치에 도달한 경우
        if current == k:
            return visited[current] - 1

        # -1로 이동
        if 0 <= current - 1 < MAX_SIZE and visited[current - 1] == 0:
            queue.append(current - 1)
            visited[current - 1] = visited[current] + 1

        # +1로 이동
        if 0 <= current + 1 < MAX_SIZE and visited[current + 1] == 0:
            queue.append(current + 1)
            visited[current + 1] = visited[current] + 1

        # *2로 순간이동
        if 0 <= current * 2 < MAX_SIZE and visited[current * 2] == 0:
            queue.append(current * 2)
            visited[current * 2] = visited[current] + 1

n, k = map(int, input().split())
print(bfs(n, k))