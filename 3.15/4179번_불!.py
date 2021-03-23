from collections import deque
import copy

n, m = map(int, input().split())

maze = []
for i in range(n):
    row = list(input().strip())
    maze.append(row)
    if "J" in row:
        Jlocate = [i, row.index("J")]
    if "F" in row:
        Flocate = [i, row.index("F")]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue =deque()
    queue.append((x,y))
    global n, maze
    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    while queue:

        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == "#":
                continue
            if visited[nx][ny] == True:
                continue
            if maze[nx][ny] == "." or maze[nx][ny] == "F" or maze[nx][ny] == "J":
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph

fire = copy.deepcopy(bfs(Flocate[0], Flocate[1]))

jihoon = copy.deepcopy(bfs(Jlocate[0], Jlocate[1]))

pos = []

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or i == n - 1 or j == m - 1:

            if jihoon[i][j] <= fire[i][j] and jihoon[i][j] != 0:
                pos.append(jihoon[i][j] + 1)



if not pos:
    print("IMPOSSIBLE")
else:
    print(min(pos))
