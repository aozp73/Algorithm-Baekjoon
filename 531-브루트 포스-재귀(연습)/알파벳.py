import sys
input = sys.stdin.readline

def dfs(x, y, path):
    global result
    result = max(result, len(path))
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in path:
            dfs(nx, ny, path + board[nx][ny])

# main
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0
dfs(0, 0, board[0][0])
print(result)
