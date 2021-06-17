from collections import deque

n = int(input())

graph = []

dx, dy = [-1, 1, 0, 0], [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int, input().strip())))
# print(graph)
def bfs(x, y, cnt):

    q = deque()

    q.append((x, y))

    graph[x][y] = cnt
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                visited[nx][ny] = 1
                graph[nx][ny] = cnt
                q.append((nx, ny))


cnt = 1

visited = [[0 for _ in range(n)] for _ in range(n)]
flag = False
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            visited[i][j] = True
            continue
        if visited[i][j] == 0:
            flag = True
            bfs(i, j, cnt)
            cnt += 1

# for i in range(n):
#     print(graph[i])
#

if not flag:
    print(0)
    exit()
print(cnt - 1)
newgraph = []
for i in range(n):
    newgraph += graph[i]
sorting = []
for i in range(1, cnt):
    sorting.append(newgraph.count(i))
    # print(newgraph.count(i))
sorting.sort()
for i in range(len(sorting)):
    print(sorting[i])
