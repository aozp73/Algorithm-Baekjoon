def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return is_prime

def count_goldbach_partitions(n, is_prime):
    cnt = 0
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            cnt += 1
            
    return cnt


t = int(input())
test_cases = [int(input()) for _ in range(t)]

# t의 최대값에 대해 미리 소수들을 구함
max_n = max(test_cases)
is_prime = eratosthenes(max_n)

for n in test_cases:
    print(count_goldbach_partitions(n, is_prime))