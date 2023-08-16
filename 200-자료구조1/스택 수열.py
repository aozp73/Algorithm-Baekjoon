n = int(input())
stack = []
result = []
cnt = 1
flag = True

for _ in range(1, n + 1):
    data = int(input())
    
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        result.append("+")

    if stack[-1] == data:
        stack.pop()
        result.append("-")
    else:  
        flag = False
        break

if flag:
    for i in result:
        print(i)
else:
    print("NO")
