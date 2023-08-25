n = int(input())
postfix = input().rstrip()
values = [0] * n
for i in range(n):
    values[i] = int(input())

stack = []
for ch in postfix:

    if 'A' <= ch <= 'Z':
        stack.append(values[ord(ch) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)
            
result = stack[0]
print("{:.2f}".format(result))
