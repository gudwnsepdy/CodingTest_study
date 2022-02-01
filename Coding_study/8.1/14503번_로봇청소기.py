def change_dir():
    global d
    d = d - 1
    if d < 0:
        d = 3

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
visited = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    visited.append([False for _ in range(m)])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn_cnt = 0

while(1):
    print(x, y)
    visited[x][y] = True
    nx = x + dx[d]
    ny = y + dy[d]

    # a
    if graph[nx][ny] != 1 and not visited[nx][ny]:
        change_dir()
        x, y = nx, ny
        turn_cnt = 0
        print("a")
        continue

    # c, d
    if turn_cnt >= 3:
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] == 1:
            break
        if 0 < nx < n and 0 < ny < m and not graph[nx][ny] and not visited[nx][ny]:
            x, y = nx, ny
            turn_cnt = 0
            print("C")
            continue

    # b
    if graph[nx][ny] == 1 or visited[nx][ny]:
        change_dir()
        turn_cnt += 1
        print("b")
        continue



res = 0
for i in range(n):
    for j in range(m):
       if visited[i][j]:
           res += 1
print(res)
for i in range(n):
    print(visited[i])