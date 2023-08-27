import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

n = input().rstrip()
check_list = list(map(int, input().split()))
cnt = 0
for num in check_list:
    if isPrime(num):
        cnt += 1
        
print(cnt)