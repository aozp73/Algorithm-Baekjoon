# 최대 연속된 사탕 개수를 찾는 함수
def check(board):
    n = len(board)
    ans = 1
    for i in range(n):
        # 각 행에서 가장 긴 연속 부분 체크
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
                
        # 각 열에서 가장 긴 연속 부분 체크      
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
    return ans

n = int(input())
board = [list(input()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n-1):
        # 가로로 인접한 두 칸 바꾸기
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        temp = check(board)
        if temp > ans:
            ans = temp
        # 원상복구
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
    
        # 세로로 인접한 두 칸 바꾸기
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        temp = check(board)
        if temp > ans:
            ans = temp
        # 원상복구
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(ans)