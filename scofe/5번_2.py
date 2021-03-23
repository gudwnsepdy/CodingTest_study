import copy
n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(input().strip()))
backup_graph = copy.deepcopy(graph)
for j in range(n):
    graph = copy.deepcopy(backup_graph)
    if graph[0][j] == "c":

def dfs(x,y):
    if x <= -1 or x >= m or y <= -1 or y >=n:
        return False
    if graph[x][y] == "."