from collections import deque
import copy
k = int(input())
w, h = map(int,input().split())

graph = []
for _ in range(h):
    graph.append(list(map(int,input().split())))

row = []
tmp = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            row.append(0)
        else:
            row.append(1)
    tmp.append(row)
    row = []

graph = copy.deepcopy(tmp)

def horse(i,j):
    if (graph[i][j] == 1 and graph[i + 1][j+1] == 1 and graph[i+1][j] == 1 )or (graph[i][j] == 1 and graph[i + 1][j + 1] == 1 and graph[i][j +1] == 1):
        return True
    else:
        return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global k, graph
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()

        if horse(x, y) and k != 0:

            nx1 = x + 2
            ny1 = y + 1
            if graph[nx1][ny1] == 1:

                graph[nx1][ny1] = graph[x][y] + 1
                q.append((nx1, ny1))
            nx2 = x + 1
            ny2 = y + 2
            if graph[nx2][ny2] == 1:
                graph[nx2][ny2] = graph[x][y] + 1
                q.append((nx2, ny2))
            k -= 1

        else:
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]

                if nx < 0 or ny < 0 or nx >= w or ny >= h:
                    continue
                if graph[nx][ny] == 0:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

    return graph[w-1][h-1]


print(bfs(0,0) - 1)
