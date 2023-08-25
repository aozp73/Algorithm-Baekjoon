n = int(input())
arr = list(map(int, input().split()))


freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

stack = []
ngf = [-1] * n

for i in range(n):
    while stack and freq[arr[stack[-1]]] < freq[arr[i]]:
        ngf[stack.pop()] = arr[i]
    stack.append(i)

print(*ngf)
