def solution(graphs):
    graphs = str(graphs)
    answer = []
    waiting = []
    for i in range(len(graphs)):
        if graphs[i] == "P" or graphs[i] == "O" or graphs[i] == "X":
            waiting.append(graphs[i])

    n = len(waiting) // 25

    room = [[] for _ in range(n)]
    for i in range(n):
        for j in range(5):
            room[i].append(waiting[:5])
            del waiting[:5]


    def check(each,i,j):
        # 상하좌우
        if (i + 1) != 5:
            if each[i + 1][j] == "P":
                print(1,i,j)
                return False
        if (j + 1) != 5:
            if each[i][j + 1] == "P":
                print(2,i,j)
                return False
        if (i - 1) != -1:
            if each[i - 1][j] == "P":
                print(3,i,j)
                return False
        if (j - 1) != -1:
            if each[i][j - 1] == "P":
                print(4, i, j)
                return False

        #상하좌우 2칸씩
        if (i + 2) < 5:
            if each[i + 2][j] == "P":
                if each[i + 1][j] != "X":
                    print(5, i, j)
                    return False
        if (j + 2) < 5:
            if each[i][j + 2] == "P":
                if each[i][j + 1] != "X":
                    print(6, i, j)
                    return False
        if (i - 2) > -1:
            if each[i - 2][j] == "P":
                if each[i - 1][j] != "X":
                    print(7, i, j)
                    return False
        if (j - 2) > -1:
            if each[i][j - 2] == "P":
                if each[i][j - 1] != "X":
                    print(8, i, j)
                    return False

        # 대각선 경우
        # 왼 위
        if (i - 1) > -1 and (j - 1) > -1:
            if each[i - 1][j - 1] == "P" and not (each[i - 1][j] == "X" and each[i][j - 1] == "X"):
                print(9)
                return False
        # 왼 아래
        if (i + 1) < 5 and (j - 1) > -1:
            if each[i + 1][j - 1] == "P":
                # print(each[i + 1][j - 1])
                if not (each[i + 1][j] == "X" and each[i][j - 1] == "X"):
                    print(10)
                    return False

        # 오 위
        if (i - 1) > -1 and (j + 1) < 5:
            if each[i - 1][j + 1] == "P":
                if not (each[i - 1][j] == "X" and each[i][j + 1] == "X"):
                    print(11, i, j)
                    return False

        # 오 아래
        if (i + 1) < 5 and (j + 1) < 5:
            if each[i + 1][j + 1] == "P":
                if not (each[i + 1][j] == "X" and each[i][j + 1] == "X"):
                    print(12, i, j)
                    return False
        return True
    cnt = 1
    for each in room:
        # print(cnt)
        cnt += 1
        flag = True
        for i in range(5):
            for j in range(5):
                if each[i][j] == "P":
                    if not check(each,i,j):
                        flag = False
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([["POOOP",
                 "OXXOX",
                 "OPXPX",
                 "OOXOX",
                 "POXXP"]]))