word = input().rstrip()
res = [0] * 26

for alpha in word:
    res[ord(alpha)-ord('a')] += 1

print(" ".join(map(str, res)))