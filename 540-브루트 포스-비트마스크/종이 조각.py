import sys

input = sys.stdin.readline

# n행, m열
n, m = map(int, input().rstrip().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().rstrip())))

ans = []

for i in range(1 << n*m):
    total = 0
    # 가로합
    for row in range(n):
        rowsum = 0
        for col in range(m):
            idx = row*m + col
            if i & (1 << idx) != 0:
                rowsum = rowsum * 10 + paper[row][col]
            else:
                total += rowsum
                rowsum = 0
        total += rowsum

    # 세로합
    for col in range(m):
        colsum = 0
        for row in range(n):
            idx = row*m + col
            if i & (1 << idx) == 0: 
                colsum = colsum * 10 + paper[row][col]
            else:
                total += colsum
                colsum = 0
        total += colsum
    ans.append(total)

print(max(ans))