from collections import deque

n, k = map(int, input().split())
arr = [0 for _ in range(k * 2)]
visited = [0 for _ in range(500000)]
def bfs(i):
    global k
    q = deque([i])
    visited[i] = 1
    while q:
        v = q.popleft()
        if v == k:
            print(visited[v] - 1)
            exit()
        if v + 1 <500000:
            if not visited[v + 1]:
                q.append(v + 1)
                visited[v + 1] = visited[v] + 1
        if v - 1 >= 0:
            if not visited[v - 1]:
                q.append(v - 1)
                visited[v - 1] = visited[v] + 1
        if v * 2 < 500000:
            if not visited[v * 2]:
                q.append(v * 2)
                visited[v * 2] = visited[v] + 1

bfs(n)