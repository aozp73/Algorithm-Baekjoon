from itertools import combinations

# 모음 리스트
vowels = ['a', 'e', 'i', 'o', 'u']

# 입력
L, C = map(int, input().split())
letters = sorted(input().split())

# 암호 생성
for comb in combinations(letters, L):

    count_vowels = sum(1 for letter in comb if letter in vowels)
    count_consonants = L - count_vowels

    # 문제 조건 : 한 개 이상 모음 / 두 개 이상 자음
    if count_vowels >= 1 and count_consonants >= 2:
        print(''.join(comb))