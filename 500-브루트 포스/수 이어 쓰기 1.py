N = int(input())
cnt = 0
length = 1
start = 1

while True:
    end = start * 10 - 1  # 현재 범위의 마지막 숫자
    if N < start:
        break
    if N < end:
        end = N
    
    cnt += (end - start + 1) * length  # 총 자릿수 저장
    
    length += 1  # 현재 숫자 범위의 자릿수
    start *= 10  # 현재 범위의 시작 숫자

print(cnt)