n = int(input().rstrip())

res = [0] * (n + 1)

res[1] = 1
if n > 1:
    res[2] = 2

for i in range(3, n + 1):
    res[i] = (res[i-1] + res[i-2]) % 10007
    
print(res[n])