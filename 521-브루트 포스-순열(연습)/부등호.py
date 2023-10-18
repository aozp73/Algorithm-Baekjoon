n = int(input())
words = [input().strip() for _ in range(n)]

# 각 알파벳의 가중치 저장
alpha_weight = {}

for word in words:
    k = len(word) - 1 
    for char in word:
        if char in alpha_weight:
            alpha_weight[char] += 10 ** k
        else:
            alpha_weight[char] = 10 ** k
        k -= 1

# 가중치를 기준으로 내림차순 정렬
sorted_alpha = sorted(alpha_weight.keys(), key = lambda x: alpha_weight[x], reverse=True)

# 가중치가 높은 알파벳부터 9 내림차순으로 숫자 할당
num = 9
result = 0
for char in sorted_alpha:
    result += alpha_weight[char] * num
    num -= 1

print(result)
