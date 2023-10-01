from itertools import combinations

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:  # 입력의 마지막 줄 처리
        break

    k, *S = data  # 첫 번째 값은 k, 나머지 값들은 집합 S
    for comb in combinations(S, 6):  # 6개의 수를 선택하는 조합 생성
        print(*comb)  # 언패킹, 공백을 기준으로 출력
    print()  