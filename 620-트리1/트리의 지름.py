import sys
from collections import defaultdict

sys.setrecursionlimit(10**9) 

def dfs(start, tree, visited):
    max_distance = 0  # 최대 거리
    max_node = 0  # 최대 거리를 갖는 노드

    stack = [(start, 0)]  # (노드, 거리)

    while stack:
        node, dist = stack.pop()

        if visited[node]:
            continue

        visited[node] = True
        if dist > max_distance:
            max_distance = dist
            max_node = node

        for adj_node, adj_dist in tree[node]:
            stack.append((adj_node, dist + adj_dist))

    return max_node, max_distance

# main
n = int(input())
tree = defaultdict(list)

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))  # 무방향 그래프이므로 양쪽 모두에 추가

visited = [False] * (n+1)
farthest_node, _ = dfs(1, tree, visited)

visited = [False] * (n+1)
_, diameter = dfs(farthest_node, tree, visited)

print(diameter)