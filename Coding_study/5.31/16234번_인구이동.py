from collections import deque

n, l, r = map(int, input().split())

graph = []

dx, dy = [-1, 1, 0, 0], [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    global cnt
    global flag, l, r
    q = deque()
    q.append((x, y))
    cnt += 1

    while q:
        # print(111111)
        # for i in range(n):
        #     print(visited[i])
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if l <= abs(graph[x][y] - graph[nx][ny]) and abs(graph[x][y] - graph[nx][ny]) <= r:

                if visited[nx][ny] == 0:
                    flag =True
                    visited[x][y] = cnt
                    visited[nx][ny] = cnt
                    q.append((nx, ny))

day = 0

while(1):
    cnt = 0
    flag = False
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i,j)
                # print(i,j)




    # for i in range(n):
    #     print(visited[i])


    populations = [0 for _ in range(cnt + 1)]
    nations = [0 for _ in range(cnt + 1)]

    if not flag:
        break

    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0:
                populations[visited[i][j]] += graph[i][j]
                nations[visited[i][j]] += 1


    for i in range(cnt + 1):
        if nations[i]:
            populations[i] = populations[i] // nations[i]

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                graph[i][j] = populations[visited[i][j]]

    # print(day)
    # for i in range(n):
    #     print(graph[i])
    day += 1
print(day)