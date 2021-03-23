n = int(input())
row = list(input().strip())
dp = [0 for i in range(n)]
flag = False

for i in range(n):
    if i == 0  or i == 1:
        if int(row[i]) == 1:
            dp[i] = 1
            flag = True
            continue
        # else:
        #     dp[i] = 1
    if not flag and row[i] == 1:
        dp[i] = 1
        flag =True
        continue
    if int(row[i]) == 1:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1])
