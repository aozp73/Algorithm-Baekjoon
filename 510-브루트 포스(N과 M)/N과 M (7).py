def backtrack(arr, n, m, s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        backtrack(arr, n, m, s + [arr[i]])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() 

backtrack(nums, N, M, [])