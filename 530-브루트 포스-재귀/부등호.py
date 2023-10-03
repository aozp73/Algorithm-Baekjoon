nums = [str(num) for num in range(10)]

k = int(input())
inequality = list(input().split())

max_ans = "0"
min_ans = "9999999999"

def check_num(inequality_idx, current_nums):
    global max_ans, min_ans
    
    # 생성한 숫자 길이가 k+1과 같으면 종료
    if len(current_nums) == k + 1:
        max_ans = max(max_ans, current_nums)
        min_ans = min(min_ans, current_nums)
        return
    
    for num in nums:
        if num not in current_nums:  # 중복된 숫자가 아닐 경우만 진행
            if inequality_idx == -1:  # 첫 번째 숫자를 설정하는 경우
                check_num(0, current_nums + num)
            else:
                if inequality[inequality_idx] == "<":
                    if current_nums[-1] < num:
                        check_num(inequality_idx + 1, current_nums + num)
                elif inequality[inequality_idx] == ">":
                    if current_nums[-1] > num:
                        check_num(inequality_idx + 1, current_nums + num)

check_num(-1, "")

print(max_ans)
print(min_ans)