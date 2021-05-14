import sys

n, k = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
s, x, y = map(int, sys.stdin.readline().split())
a, b = x, y
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(s):
    newlist = []
    for num in range(k):
        num += 1
        for i in range(n):
            for j in range(n):
                if graph[i][j] != 0:
                    newlist.append([i, j, num])
    newlist = sorted(newlist, key = lambda x: x[2])
    for xy in newlist:
        x = xy[0]
        y = xy[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] != 0:
                continue
            else:
                graph[nx][ny] = graph[x][y]

# print(graph)

print(graph[a-1][b-1])