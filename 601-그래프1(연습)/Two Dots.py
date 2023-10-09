from sys import stdin
input = stdin.readline

dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def dfs(r, c, char, prev_r, prev_c, check):
    if check[r][c]:
        return True
    
    check[r][c] = True
    
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == char and (nr, nc) != (prev_r, prev_c):
            if dfs(nr, nc, char, r, c, check):
                return True
                
    return False

# main
R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
check = [[False] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if not check[r][c] and dfs(r, c, board[r][c], -1, -1, check):
            print("Yes")
            exit(0)
            
print("No")