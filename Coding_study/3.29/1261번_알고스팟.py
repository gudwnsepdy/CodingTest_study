from collections import deque

m,n = map(int, input().split())

a = [list(map(int, input())) for i in range(n)]
ch = [[-1]*m for i in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
q = deque()
q.append([0,0])
ch[0][0] = 0

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0 <= ny < m:
            if ch[nx][ny] == -1:
                if a[nx][ny] == 0:
                    ch[nx][ny] = ch[x][y]
                    q.appendleft([nx,ny])
                else:
                    ch[nx][ny] = ch[x][y] + 1
                    q.append([nx,ny])

print(ch[n-1][m-1])


