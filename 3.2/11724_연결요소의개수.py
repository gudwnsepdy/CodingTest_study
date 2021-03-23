from collections import deque
import sys


def bfs(graph, start, visited):
    delete = []
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        delete.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return delete


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
cnt = 0
cc = []
for i in range(1, n + 1):
    if i in cc:
        continue
    delete = bfs(graph, i, visited)
    cc = cc + delete
    cnt += 1

print(cnt)
