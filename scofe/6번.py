n, m = map(int, input().split())
shop = []
for _ in range(m):
    shop.append(list(map(int,input().split())))


dp = [[0 for _ in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] == shop[i][j]
            continue
        if j == 0:

            dp[i][j] = dp[i-1][j] + shop[i][j]
            continue
        if i == 0:

            dp[i][j] = dp[i][j-1] + shop[i][j]
            continue
        dp[i][j] = max(dp[i][j-1],dp[i-1][j] ) + shop[i][j]

print(dp[m-1][n-1] + shop[0][0])