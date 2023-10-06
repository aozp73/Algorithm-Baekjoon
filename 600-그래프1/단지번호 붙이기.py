n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    graph[x][y] = 0  
    for i in range(4):  
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            count = dfs(nx, ny, count + 1)  
    return count

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(dfs(i, j, 1))

print(len(result))
for r in sorted(result):
    print(r)
