import sys
input = sys.stdin.readline

def isValid(x, y, val):
    # Row, Column Check
    for i in range(9):
        if graph[x][i] == val or graph[i][y] == val:
            return False
            
    # 3x3 Box Check
    startX, startY = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if graph[startX + i][startY + j] == val:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    x, y = blank[idx]
    for val in range(1, 10):
        if isValid(x, y, val):
            graph[x][y] = val
            dfs(idx + 1)
            graph[x][y] = 0

# main
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))
dfs(0)