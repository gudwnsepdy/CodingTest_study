n = int(input())
graph =[]

for i in range(n):
    graph.append(list(input().strip()))

visited = [[0 for _ in range(n)] for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                visited[i][j] == 1
result = 0
for visit in visited:
    result = max(result, sum(visit))


print(result)


