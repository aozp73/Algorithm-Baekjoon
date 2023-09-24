def backtrack(arr, n, m, s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        if len(s) == 0 or arr[i] >= s[-1]:
           backtrack(arr, n, m, s + [arr[i]])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() 

backtrack(nums, N, M, [])