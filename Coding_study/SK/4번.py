def solution(n, edges):
    INF = int(1e9)
    m = len(edges)
    answer = 0

    graph = [[INF] * (n) for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if a == b:
                graph[a][b] = 0
    for a, b in edges:
        graph[a][b] = 1
        graph[b][a] = 1

    for k in range(n):
        for a in range(n):
            for b in range(n):

                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for i in range(n):
        for j in  range(n):
            for k in range(n):

                if j != k and i != k and i != j and graph[i][j] == graph[j][k] + graph[i][k] and  [i,j] not in edges :
                    answer += 1
    # for i in range(n):
    #     for j in  range(n):
    #         if 0 < graph[i][j] < INF:
    #             answer += 1

    # answer -= len(edges)
    #
    # for i in range(n):
    #     print(graph[i])


    return answer


print(solution(4, [[2, 3], [0, 1], [1, 2]]))
