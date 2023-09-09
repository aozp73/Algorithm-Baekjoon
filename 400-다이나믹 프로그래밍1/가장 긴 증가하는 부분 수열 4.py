N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
dp_li = [[x] for x in A]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                dp_li[i] = dp_li[j] + [A[i]] 

max_length = max(dp) 
max_index = dp.index(max_length) 
print(max_length)
print(' '.join(map(str, dp_li[max_index])))