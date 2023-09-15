N = int(input())
A = list(map(int, input().split()))

dp1 = [1] * N
dp2 = [1] * N

# 가장 긴 증가하는 부분 수열 
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

# 가장 긴 감소하는 부분 수열 (역순)
for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

max_length = max([dp1[i] + dp2[i] - 1 for i in range(N)])

print(max_length)
