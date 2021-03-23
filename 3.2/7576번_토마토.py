from collections import deque

import sys


# n, m = map(int, sys.stdin.readline().split())
m, n = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    queue = deque()
    queue.append((x,y))
    while queue:
        print("a")
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == -1 or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            else:
                graph[nx][ny] = min(graph[x][y] + 1, graph[nx][ny])
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        print(i,j)
        if graph[i][j] == 1:
            print("1")
            bfs(i, j, graph)
print("hi")
print(graph)