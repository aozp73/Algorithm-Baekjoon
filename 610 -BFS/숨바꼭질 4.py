from collections import deque

def bfs(n, k):
    MAX_SIZE = 100001
    visited = [0] * MAX_SIZE
    prev = [-1] * MAX_SIZE # 이전 위치 기록

    queue = deque()
    queue.append(n)
    visited[n] = 1

    while queue:
        current = queue.popleft()

        if current == k:
            path = [current]
            while current != n: # 시작 위치에 도달할 때까지 경로 추적
                path.append(prev[current])
                current = prev[current]
            path.reverse()
            return visited[k] - 1, path

        for next_pos in [current-1, current+1, current*2]:
            if 0 <= next_pos < MAX_SIZE and visited[next_pos] == 0:
                queue.append(next_pos)
                visited[next_pos] = visited[current] + 1
                prev[next_pos] = current

# main
n, k = map(int, input().split())

time, path = bfs(n, k)
print(time)
print(' '.join(map(str, path)))