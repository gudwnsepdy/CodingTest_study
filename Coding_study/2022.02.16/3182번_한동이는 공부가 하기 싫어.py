n = int(input())
graph = [0]
visited = [False for _ in range(n + 1)]

for i in range(n):
    graph.append(int(input()))
cnt_list = []
def dfs(v):
    global cnt
    cnt += 1
    visited[v] = True
    if not visited[graph[v]]:
        dfs(graph[v])
    return cnt


for i in range(1, n + 1):
    cnt = 0
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    dfs(i)
    cnt_list.append(cnt)

print(cnt_list.index(max(cnt_list))+1)