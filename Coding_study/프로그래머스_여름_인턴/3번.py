def solution(maps, p, r):
    answer = 0
    l = len(maps[0])



    def dfs1(x, y, cnt):
        if cnt > r // 2:
            return
        cnt += 1
        if x <= -1 or x >= l or y <= -1 or y >= l:
            return
        if not visitied[x][y]:
            visitied[x][y] = 1

            if cnt == r // 2:
                graph[x][y] -= p / 2
                return
            graph[x][y] -= p

            dfs1(x - 1, y, cnt)
            dfs1(x, y - 1, cnt)

    def dfs2(x, y, cnt):
        if cnt >= r // 2:
            return
        cnt += 1
        if x <= -1 or x >= l or y <= -1 or y >= l:
            return
        if not visitied[x][y]:
            visitied[x][y] = 1

            if cnt == r // 2:
                graph[x][y] -= p / 2
                return
            graph[x][y] -= p
            dfs2(x + 1, y, cnt)
            dfs2(x, y - 1, cnt)

    def dfs3(x, y, cnt):

        if cnt >= r // 2:
            return
        cnt += 1
        if x <= -1 or x >= l or y <= -1 or y >= l:
            return
        if not visitied[x][y]:
            visitied[x][y] = 1

            if cnt == r // 2:
                graph[x][y] -= p / 2
                return
            graph[x][y] -= p
            dfs3(x + 1, y, cnt)
            dfs3(x, y + 1, cnt)

    def dfs4(x, y, cnt):
        if cnt >= r // 2:
            return
        cnt += 1
        if x <= -1 or x >= l or y <= -1 or y >= l:
            return
        if not visitied[x][y]:
            visitied[x][y] = 1

            if cnt == (r // 2):
                graph[x][y] -= p / 2
                return
            graph[x][y] -= p
            dfs4(x - 1, y, cnt)
            dfs4(x, y + 1, cnt)
    maxValue = 0

    for i in range(l):
        for j in range(l):
            graph = [item[:] for item in maps]
            visitied = [[0 for _ in range(l)] for _ in range(l)]
            dfs1(i-1, j-1, 0)

            dfs2(i, j-1, 0)

            dfs3(i, j, 0)

            dfs4(i-1, j, 0)

            # zero = len(list(filter(lambda n: n <= 0, graph)))

            zero = 0
            for a in range(l):
                for b in range(l):
                    if graph[a][b] <= 0:
                        zero += 1

            # if i == 4 and j== 3:
            #
            #     for i in range(l):
            #         print(graph[i])
            if zero >= maxValue:
                maxValue = zero
    # graph = [item[:] for item in maps]
    # dfs(5,4,0)
    # print(graph)
    i = 4
    j = 3
    graph = [item[:] for item in maps]
    visitied = [[0 for _ in range(l)] for _ in range(l)]
    dfs1(i - 1, j - 1, 0)

    dfs2(i, j - 1, 0)

    dfs3(i, j, 0)

    dfs4(i - 1, j, 0)
    # for i in range(l):
    #     print(graph[i])

    answer = maxValue





    return answer


print(solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]],19,6))