n = int(input())
arr = list(map(int,input().split()))
maxValue = -1e9
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))