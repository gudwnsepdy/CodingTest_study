# import sys
# input = sys.stdin.readline()
n = int(input())

arr = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if dp[i] == dp[i+1]:
        dp[i][i+1] = 1

for l in range(2,n):
    for i in range(n-l):
        if arr[i] == arr[i+l] and dp[i+1][i+l-1] == 1:
            dp[i][i+l] = 1

q = int(input())

for _ in range(q):
    a, b = map(int,input().split())
    print(dp[a-1][b-1])