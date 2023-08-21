def get_precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def to_postfix(expression):
    result = ''
    stack = []
    
    for ch in expression:
        if 'A' <= ch <= 'Z':  # 피연산자인 경우
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # '(' 제거
        else:  # 연산자인 경우
            while stack and get_precedence(stack[-1]) >= get_precedence(ch):
                result += stack.pop()
            stack.append(ch)

    while stack:
        result += stack.pop()

    return result

expression = input().rstrip()
print(to_postfix(expression))
