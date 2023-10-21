def energy_collect(arr):
    # 기저조건: 구슬 2개만 남을 경우
    if len(arr) == 2:
        return 0
    
    max_energy = 0

    # 탐색 (첫 번째, 마지막 구슬 제외) 
    for i in range(1, len(arr) - 1):
        # 현재 구슬을 제거하면서 얻을 수 있는 에너지
        current_energy = arr[i - 1] * arr[i + 1]
        
        # 최대 에너지 갱신
        new_arr = arr[:i] + arr[i+1:]        
        total_energy = current_energy + energy_collect(new_arr)
        max_energy = max(max_energy, total_energy)
    
    return max_energy

# main
N = int(input())
arr = list(map(int, input().split()))

print(energy_collect(arr))
