# 뱀 상성 전자 sw역량 테스트

N = int(input())  # 보드의 크기
K = int(input())  # 사과의 갯수

map1 = [[0] * N for i in range(N)]  # 맵을 0으로 초기화
if K > 0:
    for i in range(K):  # 사과의 좌표
        x, y = map(int, input().split())
        map1[x - 1][y - 1] = 2  # 사과과 들어있는 좌표를 2로 변경

new_map = [[1] * (N + 2) for _ in range(N + 2)]  # 벽이 있은 새로운 map을 설정해주고
for i in range(N):
    for j in range(N):
        new_map[1 + i][1 + j] = map1[i][j]  # 원래 map 값을 다시 넣어줌

new_map.append([1 for i in range(N)])
# for i in range(N + 2):
#     print(new_map[i])
L = int(input())  # 뱀의 방향 변환 정보
snake_move = []
for i in range(L):  # 뱀이 몇초후에 어느방향으로 가는지 입력 받아서 list에 저장
    ssec, smov = input().split()
    snake_move.append((int(ssec), smov))

dx = [-1, 0, 1, 0]  # 위 = 0 아래 = 2 좌 = 1 우 = 3
dy = [0, -1, 0, 1]  # 위, 좌, 아래, 우



# def turnsnake(see,)
lsave = []
see = 3  # 방향정보

initx, inity = 1, 1  # 뱀의 초기 위치

lsave.append((initx, inity))
new_map[initx][inity] = 1  # 초기 위치를 1로 만듦

_time = 0
while True:
    _time += 1  # 시간이 1초 흐름
    # snake 의 다음 위치
    nx = initx + dx[see]
    ny = inity + dy[see]
    # print((nx, ny), lsave)
    if (nx, ny) in lsave:
        break
    # 사과가 있을 때 없을 때 그리고 벽이 나왔을 때
    if new_map[nx][ny] == 0:  # 다음이 빈칸일떼
        lsave.append((nx, ny))
        new_map[nx][ny] = 1
        del_x, del_y = lsave.pop(0)
        new_map[del_x][del_y] = 0

    elif new_map[nx][ny] == 2:  # 사과가 있을 때
        lsave.append((nx, ny))
        new_map[nx][ny] = 1

    elif new_map[nx][ny] == 1:
        break
    # print(lsave)



    initx, inity = nx, ny

    # # 방향 전환이 됐을때
    for i in range(len(snake_move)):
        if _time == snake_move[i][0]:
            if snake_move[i][1] == 'L':
                # print(snake_move[i][1], _time)
                see += 1
                if see > 3:
                    see = 0
            elif snake_move[i][1] == 'D':
                # print(snake_move[i][1], _time)
                see -= 1
                if see < 0:
                    see = 3

print(_time)