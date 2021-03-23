n, m, r = map(int, input().split())
items = list(map(int,input().split()))

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0


for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

farming = []

# for i in range(n):
#     farming.append(0)

for a in range(1, n + 1):
    total = 0
    for b in range(1, n + 1):
        # if graph[a][b] > m:
            # print("no", end=" ")
        if graph[a][b] <= m:
            # print(graph[a][b], end=" ")
            total += items[b - 1]
    farming.append(total)
    # print()







print(max(farming))