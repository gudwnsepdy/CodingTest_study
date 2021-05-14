n, m = map(int, input().split())

# items = list(map(int,input().split()))

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0


for _ in range(m):
    a, b = map(int, input().split())
    graph[b][a] = 1


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

hack = [0 for _ in range(m + 1)]

# for i in range(n):
#     farming.append(0)

for a in range(1, n + 1):
    total = 0
    for b in range(1, n + 1):
        if graph[a][b] != INF:
            # print("no", end=" ")
            # print(graph[a][b], end=" ")
            hack[a - 1] += 1
    # print()


# print(hack)

max_value = max(hack)

for i in range(m+1):
    if hack[i] == max_value:
        print(i + 1, end=" ")

# print(max(farming))
