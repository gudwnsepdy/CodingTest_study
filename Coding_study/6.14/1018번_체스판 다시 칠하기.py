n, m = map(int, input().split())

chessBoard = []
for i in range(n):
    chessBoard.append(list(input().strip()))
minValue = 1000
def check(x,y):
    global minValue
    rowColor = chessBoard[x][y]
    if rowColor == "W":
        rowColor = "B"
    else:
        rowColor = "W"
    cnt = 0
    for i in range(8):
        if rowColor == "W":
            rowColor = "B"
            color = "B"
        else:
            rowColor = "W"
            color = "W"
        for j in range(8):
            if chessBoard[x + i][y + j] != color:
                cnt += 1
            if color == "W":
                color = "B"
            else:
                color = "W"
    if cnt < minValue:
        minValue = cnt
def check2(x,y):
    global minValue
    rowColor = chessBoard[x][y]

    cnt = 0
    for i in range(8):
        if rowColor == "W":
            rowColor = "B"
            color = "B"
        else:
            rowColor = "W"
            color = "W"
        for j in range(8):
            if chessBoard[x + i][y + j] != color:
                cnt += 1
            if color == "W":
                color = "B"
            else:
                color = "W"
    if cnt < minValue:
        minValue = cnt
for i in range(n):
    for j in range(m):
        if i + 7 < n and j + 7 < m:
            check(i,j)
            check2(i, j)

print(minValue)