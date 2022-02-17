from collections import deque
n, k = map(int, input().split())
arr = deque([i for i in range(1,n+1)])
res = []
while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    res.append(arr.popleft())
s = "<"
for i in res:
    s += str(i)
    s += ", "
s = s[:len(s) - 2] + ">"
print(s)