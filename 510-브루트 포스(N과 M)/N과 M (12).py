def backtrack(arr, n, m, s, start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n):
        backtrack(arr, n, m, s + [arr[i]], i)
        
N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
backtrack(nums, len(nums), M, [], 0)
