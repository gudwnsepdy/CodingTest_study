import sys
from collections import deque

r, c = map(int, input().split())
total = []
for _ in range(r):
    total.append(list(input().strip()))

sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check = dict()
dq = deque()

def DFS(x, y, w , n):
    global Fail, Succ

    if (x, y) in check and check[(x, y)]:
        Fail += w
        return
    if n == N:
        Succ += w
        return

    check[(x, y)] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        DFS(nx, ny, w*PC[k], n+1)
    check[(x, y)] = False


DFS(0, 0, 1, 0)