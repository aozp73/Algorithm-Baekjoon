# n!의 끝자리 0의 개수 구하는 함수
def count_factor(n, factor):
    cnt = 0
    while n > 0:
        n //= factor
        cnt += n
    return cnt

# 스크립트 시작점
n, m = map(int, input().split())

count_n_5 = count_factor(n, 5)
count_m_5 = count_factor(m, 5)
count_n_m_5 = count_factor(n - m, 5)

count_n_2 = count_factor(n, 2)
count_m_2 = count_factor(m, 2)
count_n_m_2 = count_factor(n - m, 2)

count_5 = count_n_5 - count_m_5 - count_n_m_5
count_2 = count_n_2 - count_m_2 - count_n_m_2

result = min(count_5, count_2)
print(result)