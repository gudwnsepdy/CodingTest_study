def clock(i):
    gear_flag[i] = True
    tmp_gear = gear[i][:]
    gear[i] = [tmp_gear[7], tmp_gear[0], tmp_gear[1], tmp_gear[2], tmp_gear[3], tmp_gear[4], tmp_gear[5], tmp_gear[6]]

    if i - 1 >= 0:
        if not gear_flag[i - 1]:
            gear_flag[i - 1] = True
            if tmp_gear[6] != gear[i - 1][2]:
                anti_clock(i - 1)
    if i + 1 < 4:
        if not gear_flag[i + 1]:
            gear_flag[i + 1] = True
            if tmp_gear[2] != gear[i + 1][6]:
                anti_clock(i + 1)


def anti_clock(i):
    gear_flag[i] = True
    tmp_gear = gear[i][:]
    gear[i] = [tmp_gear[1], tmp_gear[2], tmp_gear[3], tmp_gear[4], tmp_gear[5], tmp_gear[6], tmp_gear[7], tmp_gear[0]]
    if i - 1 >= 0:
        if not gear_flag[i - 1]:
            gear_flag[i - 1] = True
            if tmp_gear[6] != gear[i - 1][2]:
                clock(i - 1)
    if i + 1 < 4:
        if not gear_flag[i + 1]:
            gear_flag[i + 1] = True
            if tmp_gear[2] != gear[i + 1][6]:
                clock(i + 1)


gear = []
for i in range(4):
    gear.append(list(map(int, input().strip())))

n = int(input())
command = []
for i in range(n):
    command.append(list(map(int, input().split())))

# 0번째 인덱스가 왼쪽 톱니 4번째 인덱스 오른쪽 톱니
# 1번 톱니바퀴의 4번째 2번의 0번 비교
# 2번 4번째와 3번의 0번 비교
# 3번 4번째와 4번의 0번 비교


# c[0] 톱니 번호 c[1] 1이면 시계 -1이면 반시계
for c in command:
    gear_flag = [False, False, False, False]
    if c[1] == 1:
        clock(c[0] - 1)
        gear_flag[c[0] - 1] = True

    else:
        anti_clock(c[0] - 1)
        gear_flag[c[0] - 1] = True



res = 0

if gear[0][0]:
    res += 1
if gear[1][0]:
    res += 2
if gear[2][0]:
    res += 4
if gear[3][0]:
    res += 8

print(res)
