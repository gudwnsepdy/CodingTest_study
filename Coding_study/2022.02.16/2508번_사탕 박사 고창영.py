n = int(input())

for _ in range(n):
    t = input()
    a, b = map(int, input().split())
    graph = []

    for i in range(a):
        graph.append(list(input().strip()))

    cnt = 0
    # print(graph)
    for i in range(a):
        for j in range(b):
            try:
                if graph[i][j] == "o":
                    if graph[i][j - 1] == ">" and graph[i][j + 1] == "<" and j - 1 >= 0 and j + 1 < b:
                        cnt += 1

                    elif graph[i - 1][j] == "v" and graph[i + 1][j] == "^" and i + 1 < a and i - 1 >= 0:
                        cnt += 1

            except:
                continue
    print(cnt)

