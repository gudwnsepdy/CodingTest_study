from collections import deque

def change_direction(c):
    global direction
    if c == "L":
        direction -= 1
        if direction == -1:
            direction = 3
    else:
        direction += 1
        if direction == 4:
            direction = 0

n = int(input())
graph = [[0 for i in range(n)] for j in range(n)]

k = int(input())
appple_list = []

for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1 # 문제의 설명이 0,0 의 위치를 1행 1열이라 표시하고 있음.

change_direction_list = []

l = int(input())

for i in range(l):
    a, b = list(map(str, input().split()))
    change_direction_list.append([a, b])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
direction = 0
snake_location = deque([ [0, 0]]) # 왼쪽이 꼬리, 오른쪽이 머리
time = 0

while 1:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or ny < 0 or nx >=n or ny >= n: # 벽과 부딪히는 경우
        break
    if [nx, ny] in snake_location: # 자기 자신의 몸과 부딪히는 경우
        break
    if graph[nx][ny] == 0: # 사과가 없는 곳일 경우
        x, y = nx, ny
        snake_location.append([x, y]) # 머리 이동
        snake_location.popleft() # 꼬리 비워주기

    else: # 사과가 있는 곳일 경우
        graph[nx][ny] = 0 # 사과 먹기
        x, y = nx, ny
        snake_location.append([x, y]) # 머리 이동

    for i in change_direction_list: # 방향 전환 리스트 완탐
        if i[0] == str(time): # 지금이 돌아야할 때라면
            change_direction(i[1]) # 방향 돌리는 함수 실행
            break
print(time)