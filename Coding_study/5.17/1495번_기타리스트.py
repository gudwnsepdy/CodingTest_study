n, s, m = map(int, input().split())
arr = list(map(int,input().split()))
dp = [[] for _ in range(n)]

for i in range(n):
    if i == 0:
        if s - arr[0] >= 0:
            dp[0].append(s - arr[0])
        if s + arr[0] <= m:
            dp[0].append(s + arr[0])
        dp[0] = set(dp[0])
        if len(dp[0]) == 0:
            print(-1)
            exit()
    else:
        for j in dp[i - 1]:
            if j - arr[i] >= 0:
                dp[i].append(j - arr[i])
            if j + arr[i] <= m:
                dp[i].append(j + arr[i])
        dp[i] = set(dp[i])
        if len(dp[i]) == 0:
            print(-1)
            exit()



print(max(dp[-1]))
