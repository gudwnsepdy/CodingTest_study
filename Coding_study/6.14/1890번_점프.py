n = int(input())
graph = []
dp = [[0 for i in range(n)] for _ in range(n)]
# print(dp)
for i in range(n):
    graph.append(list(map(int, input().split())))
dp[0][graph[0][0]] = 1
dp[graph[0][0]][0] = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] != 0 and graph[i][j] != 0:
            if j + graph[i][j] < n:
                dp[i][j + graph[i][j]] += dp[i][j]
            if i + graph[i][j] < n:
                dp[i + graph[i][j]][j] += dp[i][j]



print(dp[n-1][n-1])
# for i in range(n):
#     print(dp[i])