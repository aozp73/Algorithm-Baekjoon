s = input().strip()
stack = []
answer = 0

for i in range(len(s)):
    if s[i] == '(': # '('
        stack.append('(') # 쇠막대기 or 레이저 저장
    else:           # ')'
        # 이전 문자가 '('일 경우, 레이저 시작 부분
        if s[i-1] == '(':
            stack.pop()  # 레이저 괄호 제거
            answer += len(stack)  # 레이저로 잘린 부분 카운트
        # 이전 문자가 ')'일 경우, 막대기의 끝
        else:
            stack.pop() # 쇠막대기 제거
            answer += 1  # 막대기 하나의 남은 오른쪽 부분 카운트

print(answer)
