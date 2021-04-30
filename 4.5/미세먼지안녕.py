import math
from collections import deque
r, c, t = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int,input().split())))


def pure_upper(a,c):
    global graph
    temp_list = []
    for i in range(1, c):
        temp_list.append(graph[a][i])
    for i in range(a - 1, -1, -1):
        temp_list.append(graph[i][c - 1])
    for i in range(c - 2, - 1, -1):
        temp_list.append(graph[0][i])
    for i in range(1, a):
        temp_list.append(graph[i][0])

    temp_list.insert(0, 0)
    del temp_list[-1]

    q = deque(temp_list)


    for i in range(1, c):
        graph[a][i] = q.popleft()
    for i in range(a - 1, -1, -1):
        graph[i][c - 1] = q.popleft()
    for i in range(c - 2, - 1, -1):
        graph[0][i] = q.popleft()
    for i in range(1, a):
        graph[i][0] = q.popleft()

def pure_lower(a,c):
    temp_list = []
    for i in range(1, c):
        temp_list.append(graph[a][i])

    for i in range(a + 1, r - 1):
        temp_list.append(graph[i][c - 1])
    for i in range(c - 1, - 1, -1):
        temp_list.append(graph[r - 1][i])
    for i in range(r - 2, a - 1, -1):
        temp_list.append(graph[i][0])

    temp_list.insert(0, 0)
    del temp_list[-1]

    q = deque(temp_list)


    for i in range(1, c):
        graph[a][i] = q.popleft()
    for i in range(a + 1, r - 1):
        graph[i][c - 1] = q.popleft()
    for i in range(c - 1, - 1, -1):
        graph[r - 1][i] = q.popleft()
    for i in range(r - 2, a - 1, -1):
        graph[i][0] = q.popleft()
    graph[a][0] = -1


for _ in range(t):
    pure = []
    plus = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 or graph[i][j] != -1 and graph[i][j] >= 5:

                cnt = 0

                if 0 <= i - 1 < r and 0 <= j < c and graph[i - 1][j] != -1:
                    plus.append([i - 1, j, math.floor(graph[i][j] / 5)])
                    cnt += 1

                if 0 <= i < r and 0 <= j - 1 < c and graph[i][j - 1] != -1:
                    plus.append([i, j - 1, math.floor(graph[i][j] / 5)])
                    cnt += 1

                if 0 <= i + 1 < r and 0 <= j < c and graph[i + 1][j] != -1:
                    plus.append([i + 1, j, math.floor(graph[i][j] / 5)])
                    cnt += 1

                if 0 <= i < r and 0 <= j + 1 < c and graph[i][j + 1] != -1:
                    plus.append([i, j + 1, math.floor(graph[i][j] / 5)])
                    cnt += 1

                graph[i][j] = graph[i][j] - math.floor(graph[i][j] / 5) * cnt
                if graph[i][j] <= 0:
                    graph[i][j] = 0
            if graph[i][j] == -1:
                pure.append([i,j])



    for x, y , z in plus:
        graph[x][y] += z
    pure_cnt = 1

    for a, b in pure:
        if pure_cnt == 1:
            pure_upper(a,c)
            pure_cnt += 1
        else:
            pure_lower(a,c)

total = 0
for i in range(r):
    total += sum(graph[i])
print(total + 2)