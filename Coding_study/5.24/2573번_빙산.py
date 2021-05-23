import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def iceBurg(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if melting[x][y] == 0:
        melting[x][y] = 1
        iceBurg(x - 1, y)
        iceBurg(x, y - 1)
        iceBurg(x + 1, y)
        iceBurg(x, y + 1)
        return True
    return False

def melt(x, y):
    cnt = 0
    if x - 1 >= 0:
        if graph[x - 1][y] == 0:
            cnt += 1
    if x + 1 < n:
        if graph[x + 1][y] == 0:
            cnt += 1
    if y - 1 >= 0:
        if graph[x][y - 1] == 0:
            cnt += 1
    if y + 1 < m:
        if graph[x][y + 1] == 0:
            cnt += 1

    melting[x][y] = cnt

year = 0

while(1):
    # print(year, "a")
    year += 1
    melting = [[0 for _ in range(m)] for _ in range(n)]
    # new_graph = [[1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                melt(i, j)

    for i in range(n):
        for j in range(m):
            graph[i][j] -= melting[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
            if graph[i][j] != 0:
                # new_graph[i][j] = 0
                melting[i][j] = 0
            else:
                melting[i][j] = 1

    iceCnt = 0
    zeroCnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                if iceBurg(i,j):
                    iceCnt += 1
            else:
                zeroCnt += 1
    if zeroCnt == n * m:
        print(0)
        exit()
    if iceCnt >= 2:
        break


print(year)