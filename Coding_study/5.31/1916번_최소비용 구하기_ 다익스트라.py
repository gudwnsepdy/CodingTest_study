import sys
input = sys.stdin.readline
INF = int(987654321)

n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)


input_list = []
for _ in range(m):
    flag = True
    a, b, c = map(int, input().split())
    # print(graph[a], len(graph[a]))
    if len(graph[a]) >= 1:
        for i in range(len(graph[a])):
            if graph[a][i][0] == b:
                # print("AA")
                graph[a][i][1] = min(c, graph[a][i][1])
                flag = False
                continue

        if flag:
            graph[a].append([b,c])

    else:
        graph[a].append([b, c])

#     print(graph)
# print(graph)
start, destination = map(int, input().split())

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def di(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

di(start)

print(distance[destination])