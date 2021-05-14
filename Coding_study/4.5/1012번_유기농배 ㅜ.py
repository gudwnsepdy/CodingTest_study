import sys
sys.setrecursionlimit(10**6)

t = int(input())
for case in range(t):
    m, n, k = map(int,input().split())

    graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    result = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    print(result)
