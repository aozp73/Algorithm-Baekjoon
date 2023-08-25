n = int(input())
arr = list(map(int, input().split()))

stack = []
res = [-1] * n

for i in range(n):    
    while stack and arr[stack[-1]] < arr[i]:
        res[stack.pop()] = arr[i]
        
    stack.append(i)

print(*res)
