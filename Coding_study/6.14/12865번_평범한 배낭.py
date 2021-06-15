import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weight = [0]
gold = [0]
for i in range(n):
    w, g = map(int, input().split())
    weight.append(w)
    gold.append(g)

dp = [[0 for i in range(k + 1)] for _ in range(n + 1)]

for w in range(1, n + 1):
    for i in range(1, k + 1):
        if i >= weight[w]:
            dp[w][i] = max(dp[w - 1][i], dp[w - 1][i - weight[w]] + gold[w])
        else:
            dp[w][i] = dp[w-1][i]

print(dp[n][k])

#출처 : https://kils-log-of-develop.tistory.com/247