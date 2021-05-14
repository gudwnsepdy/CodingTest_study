n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
cnt = [0, 0, 0]

post = []

def check(k, x, y):

    global cnt
    flag = graph[x][y]
    for i in range(k):
        for j in range(k):
            if (graph[i + x][j + y] != flag):
                for a in range(3):
                    for b in range(3):
                        check(k//3, x + (a * k//3), y + (b * k//3))
                return
    # if [x,y] not in post:
    #     post.append([x,y])
        # print(flag,k,x,y)
    cnt[flag + 1] += 1

    return


check(n, 0, 0)

for i in range(3):
    print(cnt[i])

