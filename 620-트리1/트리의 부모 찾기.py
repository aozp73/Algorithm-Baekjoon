import sys
sys.setrecursionlimit(10**9)  # 재귀 깊이 설정

def dfs(current, tree):
    for child in tree[current]:
        if parents[child] == 0:  # 부모가 아직 정해지지 않았다면
            parents[child] = current  # 부모를 정하고
            dfs(child, tree)  # 계속 DFS 수행

# main
N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N+1)]

# 트리 정보 입력 받기
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (N+1)
parents[1] = 1  # 루트의 부모 자기 자신으로 설정

# 각 노드의 부모 찾기
dfs(1, tree)

for i in range(2, N+1):
    print(parents[i])