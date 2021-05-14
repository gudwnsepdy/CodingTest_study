from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    res = 0
    while queue:
        v = queue.popleft()
        # print(v, end=" ")
        res += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return res

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


res = [0 for _ in range(n + 1)]
tmp = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    result = bfs(graph,i,visited)
    res[i] = result


maxv = max(res)

for i in range(1, n + 1):
    if res[i] == maxv:
        print(i, end = ' ')