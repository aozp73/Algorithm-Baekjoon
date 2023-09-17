from itertools import combinations

heights = []
for _ in range(9):
    heights.append(int(input()))

heights.sort(reverse=False)

for comb in combinations(heights, 7):  
    if sum(comb) == 100:  
        for h in comb:  
            print(h)
        break 