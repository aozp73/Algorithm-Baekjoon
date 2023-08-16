def is_vps(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return "NO"
            stack.pop()
    if stack:
        return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(is_vps(s))