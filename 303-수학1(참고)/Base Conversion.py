# A진법을 10진법으로 변환하는 함수
def to_decimal(num_list, base):
    res = 0
    for idx, num in enumerate(reversed(num_list)):
        res += num * (base ** idx)
    return res

# 10진법을 B진법으로 변환하는 함수
def to_b(num, base):
    res = []
    while num > 0:
        res.append(num % base)
        num //= base
    return reversed(res)

a, b = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))

# A진법 -> 10진법 변환
decimal_num = to_decimal(nums, a)

# 10진법 -> B진법 변환
result = to_b(decimal_num, b)

print(' '.join(map(str, result)))
