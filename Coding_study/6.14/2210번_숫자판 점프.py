import sys
sys.setrecursionlimit(10**6)


graph = []

for i in range(5):
    graph.append(list(map(str, input().split())))

res = []


def dfs(x, y, num):
    if x < 0 or y < 0 or x > 4 or y > 4:
        return
    num = num + graph[x][y]
    if len(str(num)) > 6:
        return
    if len(str(num)) == 6:

        if num not in res:
            res.append(num)
        return

    dfs(x + 1, y, num)
    dfs(x, y + 1, num)
    dfs(x - 1, y, num)
    dfs(x, y - 1, num)


for i in range(5):
    for j in range(5):
        dfs(i, j, "")
# dfs(4,3, 0)
# print(res)
print(len(res))
