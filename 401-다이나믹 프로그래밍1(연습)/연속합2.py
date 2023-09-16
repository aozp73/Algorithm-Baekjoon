N = int(input())
arr = list(map(int, input().split()))

# dp_0: i번째 원소를 제거하지 않았을 때 i번째까지의 연속합 최대값
# dp_1: i번째 원소를 제거할 기회가 있을 때 i번째까지의 연속합 최대값
dp_0, dp_1 = arr[0], arr[0]
max_sum = arr[0]

for i in range(1, N):
    dp_0, dp_1 = max(dp_0 + arr[i], arr[i]), max(dp_0, dp_1 + arr[i])
    max_sum = max(max_sum, dp_0, dp_1)

print(max_sum)