word = input().rstrip()
res = []

for i in range(len(word)):
    res += [word[i:len(word)]]
    
res.sort()

for alpha in res:
    print(alpha)