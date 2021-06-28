from collections import deque

graph = []
visited = [[False for i in range(8)] for j in range(8)]

for i in range(8):
    graph.append(list(input().strip()))

new_q = []
q = [[7, 0]]

dx = [-1, 1, 0, 0, -1, 1, -1, 1, 0]
dy = [0, 0, -1, 1, -1, 1, 1, -1, 0]
for t in range(64):
    q = deque(q)
    new_q = []
    visited = [[False for i in range(8)] for j in range(8)] # 한 타임마다 visited 초기화
    while q:
        uk = q.popleft()
        x, y = uk[0], uk[1]

        if graph[x][y] == "#": # 현재 시간에 그 지점이 벽이 되어버린 경우
            continue
        for i in range(9): # 총 9방향으로 이동 가능 상하좌우, 대각선 네칸, 그대로 있기
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 8 or ny >= 8: # 맵 벗어나면 x
                continue

            if graph[nx][ny] == "#":
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                new_q.append([nx, ny])

    if t <= 9: # 벽 아래로 한칸씩 내려주기
        for i in range(7,-1,-1): # 아래서부터 내려줘야함. 위에서부터 내리면 한번에 다 내려감
            for j in range(7,-1,-1):
                if graph[i][j] == "#":
                    if i + 1 != 8:
                        graph[i + 1][j] = "#"
                        graph[i][j] = "."
                    else:
                        graph[i][j] = "."

    q = new_q[:]

if visited[0][7]: # 오른쪽 맨위가 True면 1
    print(1)
else:
    print(0)