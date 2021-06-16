from collections import deque

n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
# print(graph)
bfsVisited = [False] * (n + 1)
dfsVisited = [False] * (n + 1)

def bfs(graph, start):
    q = deque([start])
    bfsVisited[start] = True

    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not bfsVisited[i]:
                q.append(i)
                bfsVisited[i] = True

def dfs(graph, v):
    dfsVisited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not dfsVisited[i]:
            dfs(graph, i)
dfs(graph, v)
print()
bfs(graph, v)
