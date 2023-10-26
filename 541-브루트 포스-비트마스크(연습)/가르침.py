from itertools import combinations

N, K = map(int, input().split())

if K < 5: # K가 5 미만이면 어떤 단어도 읽을 수 없으므로 0 출력
    print(0)
    exit()
elif K == 26: # K가 26이면 모든 단어를 읽을 수 있으므로 N 출력
    print(N)
    exit()

# 각 단어에서 필수 문자인 a, n, t, i, c를 제외하고 저장
# ex. [{'r'}, {'l', 'o', 'e', 'h'}, {'r'}]
words = [set(input().rstrip()[4:-4]) - {'a', 'n', 't', 'i', 'c'} for _ in range(N)]

# 가능한 문자들
available_chars = set('abcdefghijklmnopqrstuvwxyz') - {'a', 'n', 't', 'i', 'c'}

# 최대로 읽을 수 있는 단어의 수를 저장할 변수
max_count = 0

# 필요한 문자 K-5개의 조합 구하기
for comb in combinations(available_chars, K-5):
    comb = set(comb)
    count = 0
    for word in words:
        if word.issubset(comb):
            count += 1
    max_count = max(max_count, count)

print(max_count)
