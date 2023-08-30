import math

# n : 동생의 수, s: 수빈이 위치
n, s = map(int, input().split())

# 동생들의 위치
n_posi = list(map(int, input().split()))

# 수빈이 - 각 동생들 거리차 계산
distances = [abs(s - x) for x in n_posi]

# 첫 번째 거리를 초기 GCD 값으로 설정
gcd_val = distances[0]

# 모든 거리에 대해 GCD 계산
for distance in distances[1:]:
    gcd_val = math.gcd(gcd_val, distance)

print(gcd_val)