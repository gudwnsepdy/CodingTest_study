from collections import deque
from itertools import combinations
import copy
n, v = map(int,input().split())

graph =[]
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
two_cnt = 0
zero_cnt = 0
def bfs(l,new_graph):
    global n

    cnt = 0
    q = deque()
    for i in l:
        q.append(i)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if new_graph[nx][ny] == - 1:
                continue
            if new_graph[nx][ny] == 0:
                new_graph[nx][ny] = new_graph[x][y] + 1

                q.append((nx,ny))
                cnt = max(cnt, new_graph[nx][ny])
    # print(cnt)
    # print(new_graph)
    # print(l)
    for i in range(n):
        if 0 in new_graph[i]:
            cnt = 99999
    # print(cnt)
    return cnt

virus_index =[]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            two_cnt +=1
            graph[i][j] = 0
            virus_index.append([i,j])
        elif graph[i][j] == 1:
            graph[i][j] = -1
        else:
            zero_cnt += 1
all_virus = list(combinations(virus_index, v))
if two_cnt == v and zero_cnt == 0:
    print(0)
    exit()
min_val = 99999
for l in all_virus:
    new_graph = copy.deepcopy(graph)
    min_val = min(min_val,bfs(l, new_graph))
if min_val == 99999:
    print(-1)
    exit()
print(min_val)