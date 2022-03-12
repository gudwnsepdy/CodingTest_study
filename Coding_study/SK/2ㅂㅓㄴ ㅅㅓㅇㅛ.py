from collections import deque
def solution(n, clockwise):
    answer = [[0 for _ in range(n)] for  _ in range(n)]

    visited = [[0 for _ in range(n)] for i in range(n)]
    graph = [[0 for _ in range(n)] for i in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1 ,0]

    def next_coord(x, y, d):
        x = x + dx[d - 1]
        y = y + dy[d - 1]
        return x, y


    q = deque()
    if clockwise:
        q.append([0, 0, 0])
        q.append([0, n - 1, 1])
        q.append([n - 1, n - 1, 2])
        q.append([n - 1, 0, 3])
    else:
        q.append([0, 0, 1])
        q.append([0, n - 1, 2])
        q.append([n - 1, n - 1, 3])
        q.append([n - 1, 0, 0])


    answer[0][0], answer[0][n - 1], answer[n-1][0], answer[n-1][n-1] = 1,1,1,1
    while q:
        x, y ,d = q.popleft()

        nx, ny = next_coord(x, y, d)
        if 0 <= nx <n and 0 <= ny <n:
            if not answer[nx][ny]:
                answer[nx][ny] = answer[x][y] + 1
                q.append([nx, ny, d])
            else:
                if clockwise:  # 참
                    d = d + 1
                    if d > 3:
                        d = 0
                else:
                    d = d - 1
                    if d < 0:
                        d = 3
                nx, ny = next_coord(x, y, d)
                if not answer[nx][ny]:
                    answer[nx][ny] = answer[x][y] + 1
                    q.append([nx, ny, d])

    return answer

print(solution(5, True))