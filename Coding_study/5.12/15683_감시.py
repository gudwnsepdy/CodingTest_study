from itertools import product

n, m = map(int,input().split())
graph =[[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))

def cctv(case, x, y):
    cnt = 0
    if case == 1:
        # 1 오른쪾
        while(1):
            cnt += 1
            if y + cnt == m:
                break
            if newgraph[x][y + cnt] == 6:
                break
            elif newgraph[x][y + cnt] == 0:
                newgraph[x][y + cnt] = -1

    elif case == 2:
        # 2 아래쪽
        while(1):
            cnt += 1
            if x + cnt == n:
                break
            elif newgraph[x + cnt][y] == 6:
                break
            elif newgraph[x + cnt][y] == 0:
                newgraph[x + cnt][y] = -1
    elif case == 3:
        # 3 왼쪽
        while(1):
            cnt += -1
            if y + cnt == -1:
                break
            if newgraph[x][y + cnt] == 6:
                break
            elif newgraph[x][y + cnt] == 0:
                newgraph[x][y + cnt] = -1
    else:
        while(1):
            # 4 위쪽
            cnt += -1
            if x + cnt == -1:
                break
            if newgraph[x + cnt][y] == 6:
                break
            elif newgraph[x + cnt][y] == 0:
                newgraph[x + cnt][y] = -1


allCases = []
#
# for a in range(1,5):
#     for b in range(1,3):
#         for c in range(1,5):
#             for d in range(1, 5):
#                 allCases.append([a,b,c,d])

cctvCnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctvCnt += 1
# print(cctvCnt)
for i in product([1,2,3,4], repeat=cctvCnt):
    allCases.append(i)
minValue = 1e9
# print(graph)
for each in allCases:
    each = list(each)
    newgraph = [item[:] for item in graph]
    for i in range(n):
        for j in range(m):
            cell = newgraph[i][j]

            if cell == 1:
                dir = each[0]
                del each[0]
                cctv(dir,i,j)

            elif cell == 2:
                dir = each[0]
                del each[0]
                if dir == 1 or dir == 3:
                    cctv(1,i,j)
                    cctv(3,i,j)
                else:
                    cctv(2,i,j)
                    cctv(4,i,j)

            elif cell == 3:

                dir = each[0]
                del each[0]

                if dir == 1:
                    cctv(1, i, j)
                    cctv(4, i, j)
                elif dir == 2:
                    cctv(1, i, j)
                    cctv(2, i, j)
                elif dir == 3:
                    cctv(2, i, j)
                    cctv(3, i, j)
                else:
                    cctv(3, i, j)
                    cctv(4, i, j)

            elif cell == 4:
                dir = each[0]
                del each[0]

                if dir == 1:
                    cctv(4, i, j)
                    cctv(1, i, j)
                    cctv(3, i, j)
                elif dir == 2:
                    cctv(4, i, j)
                    cctv(1, i, j)
                    cctv(2, i, j)
                elif dir == 3:
                    cctv(3, i, j)
                    cctv(1, i, j)
                    cctv(2, i, j)
                else:
                    cctv(3, i, j)
                    cctv(4, i, j)
                    cctv(2, i, j)
            elif cell == 5:
                # way = each[0]
                del each[0]
                cctv(3, i, j)
                cctv(4, i, j)
                cctv(2, i, j)
                cctv(1, i, j)

    zero = 0
    for r in range(n):
        for t in range(m):
            if newgraph[r][t] == 0:
                zero += 1
    # print("*****************")
    # for idx in range(n):
    #     print(newgraph[idx])
    # print(each)
    # print("*****************")
    if zero < minValue:
        minValue = zero

print(minValue)