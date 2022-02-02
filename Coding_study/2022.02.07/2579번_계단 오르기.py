n = int(input())
l = []
d = [0 for _ in range(n)]
for _ in range(n):
    l.append(int(input()))
if n == 1:
    print(l[0])
    exit()
if n == 2:
    print(l[0] + l[1])
    exit()
d[0] = l[0]
d[1] = max(l[0] + l[1], l[1])
d[2] = max(l[0] + l[2], l[1] + l[2])

for i in range(3, n):
    d[i] = max(d[i - 2] + l[i], d[i - 3] + l[i - 1] + l[i])

print(d[-1])