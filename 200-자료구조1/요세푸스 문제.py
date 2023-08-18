from collections import deque

def josephus(n, k):
    queue = deque(range(1, n + 1))
    result = []

    while queue:
        for _ in range(k-1):
            queue.append(queue.popleft())
        result.append(queue.popleft())

    return result

n, k = map(int, input().split())
result = josephus(n, k)
print("<", end='')
print(", ".join(map(str, result)), end='')
print(">")