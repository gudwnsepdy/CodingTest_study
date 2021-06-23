n, m, x, y, k = map(int, input().split())
grpah = []

for i in range(n):
    grpah.append(list(map(int, input().split())))

command = list(map(int, input().split()))
# dice = [1,2,3,4,5,6]
dice = [0,0,0,0,0,0]
def move(c):
    global dice, x, y
    tmp_dice = dice[:]
    if c == 1:
        if y + 1 >= m:
            return
        y += 1
        dice = [tmp_dice[3], tmp_dice[1], tmp_dice[0], tmp_dice[5], tmp_dice[4], tmp_dice[2]]
        if grpah[x][y] == 0:
            grpah[x][y] = dice[5]
        else:
            dice[5] = grpah[x][y]
            grpah[x][y] = 0
    elif c == 2:
        if y - 1 < 0:
            return
        y -= 1
        dice = [tmp_dice[2], tmp_dice[1], tmp_dice[5], tmp_dice[0], tmp_dice[4], tmp_dice[3]]
        if grpah[x][y] == 0:
            grpah[x][y] = dice[5]
        else:
            dice[5] = grpah[x][y]
            grpah[x][y] = 0

    elif c == 3:
        if x - 1 < 0:
            return
        x -= 1
        dice = [tmp_dice[4], tmp_dice[0], tmp_dice[2], tmp_dice[3], tmp_dice[5], tmp_dice[1]]
        if grpah[x][y] == 0:
            grpah[x][y] = dice[5]
        else:
            dice[5] = grpah[x][y]
            grpah[x][y] = 0

    else:
        if x + 1 >= n:
            return
        x += 1
        dice = [tmp_dice[1], tmp_dice[5], tmp_dice[2], tmp_dice[3], tmp_dice[0], tmp_dice[4]]
        if grpah[x][y] == 0:
            grpah[x][y] = dice[5]
        else:
            dice[5] = grpah[x][y]
            grpah[x][y] = 0
    print(dice[0])

for i in command:
    # print(grpah)
    move(i)
