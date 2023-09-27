N = int(input())
nums = list(map(int, input().split()))

# 1. 뒤에서부터 nums[i-1] > nums[i] 를 만족하는 위치 i 찾기
i = N - 1
while i > 0 and nums[i-1] <= nums[i]:
    i -= 1

if i == 0:
    print(-1)
else:
    # 2. 뒤에서부터 nums[i-1]보다 처음으로 작은 값 찾기
    j = N - 1
    while nums[j] >= nums[i-1]:
        j -= 1

    # 3. nums[i-1]과 nums[j]의 위치 바꾸기
    nums[i-1], nums[j] = nums[j], nums[i-1]

    # 4. i부터 끝까지의 부분을 뒤집기
    nums[i:] = reversed(nums[i:])

    print(' '.join(map(str, nums)))