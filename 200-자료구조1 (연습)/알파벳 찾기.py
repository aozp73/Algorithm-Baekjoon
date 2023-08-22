word = input().rstrip()
res = [-1] * 26

for i, alpha in enumerate(word):
    val = ord(alpha) - ord('a')
    if res[val] == -1:
        res[val] = i
        
print(" ".join(map(str, res)))