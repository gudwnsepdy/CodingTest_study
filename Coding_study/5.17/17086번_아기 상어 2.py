n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

sharks = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            sharks.append([i,j])

dist_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            continue
        safety_zone = max(n-1,m-1)
        for another_shark in sharks:
            dist = max(abs(another_shark[0] - i),abs(another_shark[1] - j))
            if dist != 0 and safety_zone > dist:
                safety_zone = dist
        dist_list.append(safety_zone)

print(max(dist_list))
