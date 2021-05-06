def solution(numbers, hand):
    answer = ''
    keyMove = [[0 for _ in range(13)] for i in range(13)]
    keyMove[10][0] = 1
    keyMove[10][8] = 2
    keyMove[10][5] = 3
    keyMove[10][2] = 4

    keyMove[7][0] = 2
    keyMove[7][8] = 1
    keyMove[7][5] = 2
    keyMove[7][2] = 3

    keyMove[4][0] = 3
    keyMove[4][8] = 2
    keyMove[4][5] = 1
    keyMove[4][2] = 2

    keyMove[1][0] = 4
    keyMove[1][8] = 3
    keyMove[1][5] = 2
    keyMove[1][2] = 1

    keyMove[3][0] = 4
    keyMove[3][8] = 3
    keyMove[3][5] = 2
    keyMove[3][2] = 1

    keyMove[6][0] = 3
    keyMove[6][8] = 2
    keyMove[6][5] = 1
    keyMove[6][2] = 2

    keyMove[9][0] = 2
    keyMove[9][8] = 1
    keyMove[9][5] = 2
    keyMove[9][2] = 3

    keyMove[12][0] = 1
    keyMove[12][8] = 2
    keyMove[12][5] = 3
    keyMove[12][2] = 4

    keyMove[2][5] = 1
    keyMove[2][8] = 2
    keyMove[2][0] = 3

    keyMove[2][5] = 1
    keyMove[2][8] = 2
    keyMove[2][0] = 3

    keyMove[5][2] = 1
    keyMove[5][8] = 1
    keyMove[5][0] = 2

    keyMove[8][2] = 2
    keyMove[8][5] = 1
    keyMove[7][0] = 2

    keyMove[0][5] = 2
    keyMove[0][8] = 1
    keyMove[0][2] = 3

    l = 10
    r = 12
    lk = [1, 4, 7]
    rk = [3, 6, 9]
    for i in numbers:
        if i in lk:
            # print(l, r, i,1)
            answer += "L"
            l = i
        elif i in rk:
            # print(l, r, i,2)
            answer += "R"
            r = i
        else:
            if keyMove[r][i] < keyMove[l][i]:
                # print(l,r,i,3)
                r = i
                answer += "R"

            elif keyMove[l][i] < keyMove[r][i]:
                # print(l, r, i,4)
                l = i
                answer += "L"
            else:
                if hand == "right":
                    # print(l, r, i,5)
                    r = i
                    answer += "R"
                else:
                    # print(l, r, i,6)
                    l = i
                    answer += "L"
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))