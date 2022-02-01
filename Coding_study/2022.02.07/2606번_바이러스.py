from collections import deque
n = int(input())
t = int(input())
visited = [0 for _ in range(n)]
line = [[] for i in range(n)]
for _ in range(t):
    a, b = map(int, input().split())
    line[a-1].append(b - 1)
    line[b - 1].append(a - 1)

# print(visited)
q = deque([0])
visited[0] = 1
while q:
    v = q.popleft()
    for i in line[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = 1

cnt = 0
for i in visited:
    if i: cnt += 1
# print(visited)
if cnt == -1:
    print(0)
else:
    print(cnt - 1)