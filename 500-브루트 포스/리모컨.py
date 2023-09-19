import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
broken = set(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    str_nums = str(nums)
    
    # 모든 숫자가 고장난 버튼에 속하지 않는 경우만 검사
    if all(int(ch) not in broken for ch in str_nums):
        min_count = min(min_count, abs(nums - target) + len(str_nums))

print(min_count)
