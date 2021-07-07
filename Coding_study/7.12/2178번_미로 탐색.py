from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        # print(x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

n ,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().strip())))

visited =[[0 for i in range(m)] for j in range(n)]
bfs(0,0)
# print(graph)
print(visited[-1][-1])