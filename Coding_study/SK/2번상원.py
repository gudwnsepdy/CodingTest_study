from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 1243


def solution(n, clockwise):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    def nextDir(x, y, dir):
        x = x + dx[dir - 1]
        y = y + dy[dir - 1]
        return x, y

    def bfs(n):
        q = deque()
        if clockwise:
            q.append([0, 0, 1])
            q.append([0, n - 1, 2])
            q.append([n - 1, n - 1, 3])
            q.append([n - 1, 0, 4])
        else:
            q.append([0, 0, 2])
            q.append([0, n - 1, 3])
            q.append([n - 1, n - 1, 4])
            q.append([n - 1, 0, 1])
        answer[0][0], answer[0][n - 1], answer[n - 1][0], answer[n - 1][n - 1] = 1, 1, 1, 1
        while q:
            x, y, dir = q.popleft()

            nx, ny = nextDir(x, y, dir)
            if 0 <= nx < n and 0 <= ny < n:
                if answer[nx][ny] == 0:
                    answer[nx][ny] = answer[x][y] + 1
                    q.append([nx, ny, dir])
                else:
                    if clockwise:  # 참
                        dir = dir + 1
                        if dir > 4:
                            dir = 1
                    else:
                        dir = dir - 1
                        if dir < 1:
                            dir = 4
                    nx, ny = nextDir(x, y, dir)
                    if answer[nx][ny] == 0:
                        answer[nx][ny] = answer[x][y] + 1
                        q.append([nx, ny, dir])

    bfs(n)
    return answer


result = solution(5, True)
for i in result:
    print(i)

    # if dir == 1:
    #     nx, ny = nextDir(x, y, dir)
    #     if 0<=nx<n and 0<=ny<n:
    #         if answer[nx][ny] == 0:
    #             answer[nx][ny] = answer[x][y] + 1
    #             q.append([nx, ny, dir])
    #         else:
    #             if clockwise: #참
    #                 dir = dir + 1
    #                 if dir > 4:
    #                     dir = 1
    #             else:
    #                 dir = dir - 1
    #                 if dir < 1:
    #                     dir = 4
    #             nx, ny = nextDir(x, y, dir)
    #             q.append([nx, ny, dir])

    # elif dir == 2:
    #     nx, ny = nextDir(x, y, dir)
    #     if 0<=nx<n and 0<=ny<n:
    #         if answer[nx][ny] == 0:
    #             answer[nx][ny] = answer[x][y] + 1
    #             q.append([nx, ny, dir])
    #         else:
    #             if clockwise: #참
    #                 dir = dir + 1
    #                 if dir > 4:
    #                     dir = 1
    #             else:
    #                 dir = dir - 1
    #                 if dir < 1:
    #                     dir = 4
    #             nx, ny = nextDir(x, y, dir)
    #             q.append([nx, ny, dir])

    # elif dir == 3:
    #     nx, ny = nextDir(x, y, dir)
    #     if 0<=nx<n and 0<=ny<n:
    #         if answer[nx][ny] == 0:
    #             answer[nx][ny] = answer[x][y] + 1
    #             q.append([nx, ny, dir])
    #         else:
    #             if clockwise: #참
    #                 dir = dir + 1
    #                 if dir > 4:
    #                     dir = 1
    #             else:
    #                 dir = dir - 1
    #                 if dir < 1:
    #                     dir = 4
    #             nx, ny = nextDir(x, y, dir)
    #             q.append([nx, ny, dir])

    # else:
    #     nx, ny = nextDir(x, y, dir)
    #     if 0<=nx<n and 0<=ny<n:
    #         if answer[nx][ny] == 0:
    #             answer[nx][ny] = answer[x][y] + 1
    #             q.append([nx, ny, dir])
    #         else:
    #             if clockwise: #참
    #                 dir = dir + 1
    #                 if dir > 4:
    #                     dir = 1
    #             else:
    #                 dir = dir - 1
    #                 if dir < 1:
    #                     dir = 4
    #             nx, ny = nextDir(x, y, dir)
    #             q.append([nx, ny, dir])