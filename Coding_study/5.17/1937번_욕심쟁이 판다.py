n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(n)] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x,y,cnt):
    global maxValue
    visited[x][y] = 1
    if cnt > maxValue:
        maxValue = cnt
    if x - 1 >= 0:
        if graph[x-1][y] > graph[x][y]:
            print(x,y,1)
            if dp[x - 1][y] != 0:
                cnt += dp[x - 1][y]
                if cnt >= maxValue:
                    maxValue = cnt
            else:
                if visited[x - 1][y] == 0:
                    dfs(x-1, y, cnt + 1)
                else:
                    cnt += 1
                    if cnt >= maxValue:
                        maxValue = cnt
                    cnt -= 1
    if y - 1 >= 0:
        if graph[x][y-1] > graph[x][y]:
            print(x, y, 2)
            if dp[x][y - 1] != 0:
                cnt += dp[x][y - 1]
                if cnt >= maxValue:
                    maxValue = cnt

            else:
                if visited[x][y-1] == 0:
                    dfs(x, y - 1, cnt + 1)
                else:
                    cnt += 1
                    if cnt >= maxValue:
                        maxValue = cnt
                    cnt -= 1
    if x + 1 < n:
        if graph[x + 1][y] > graph[x][y]:
            print(x, y, 3)
            if dp[x + 1][y] != 0:
                cnt += dp[x + 1][y]
                if cnt >= maxValue:
                    maxValue = cnt
            else:
                if visited[x+1][y] == 0:
                    dfs(x + 1, y, cnt + 1)
                else:
                    cnt += 1
                    if cnt >= maxValue:
                        maxValue = cnt
                    cnt -= 1
    if y + 1 < n:
        if graph[x][y + 1] > graph[x][y]:
            print(x, y, 4)
            if dp[x][y + 1] != 0:
                cnt += dp[x][y + 1]
                if cnt >= maxValue:
                    maxValue = cnt
            else:
                if visited[x][y + 1] == 0:
                    dfs(x, y + 1, cnt + 1)
                else:
                    cnt += 1
                    if cnt >= maxValue:
                        maxValue = cnt
                    cnt -= 1

for i in range(n):
    for j in range(n):

        maxValue = 0
        dfs(i,j,0)
        # print(i,j,maxValue)
        visited[i][j] = 1
        dp[i][j] = maxValue


max_life = 0
for i in range(n):
    # print(dp[i])
    for j in range(n):
        if dp[i][j] > max_life:
            max_life = dp[i][j]

print(max_life + 1)