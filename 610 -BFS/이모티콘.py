from collections import deque

def bfs(S):
    # 1차원: 화면에 있는 이모티콘 개수 / 2차원: 클립보드에 있는 이모티콘 개수
    visited = [[False] * (S+1) for _ in range(S+1)] 
    queue = deque([(1, 0, 0)]) # (화면 이모티콘 수, 클립보드 이모티콘 수, 시간)
    
    while queue:
        screen, clipboard, time = queue.popleft()
        
        # 기저 조건: 화면의 이모티콘 수가 S개가 되면 시간 반환
        if screen == S:
            return time

        # 클립보드에 화면의 이모티콘 복사
        if not visited[screen][screen]:
            visited[screen][screen] = True
            queue.append((screen, screen, time + 1))

        # 클립보드의 이모티콘 화면에 붙여넣기
        if clipboard > 0 and screen + clipboard <= S and not visited[screen+clipboard][clipboard]:
            visited[screen+clipboard][clipboard] = True
            queue.append((screen+clipboard, clipboard, time+1))

        # 화면의 이모티콘 삭제
        if screen > 1 and not visited[screen-1][clipboard]:
            visited[screen-1][clipboard] = True
            queue.append((screen-1, clipboard, time+1))
            
    return -1

# main
S = int(input())
print(bfs(S))