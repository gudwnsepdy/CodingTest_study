n = int(input())
t = []
p = []
d = [0 for i in range(n + 1)]
for i in range(n):
    a, b = map(int,input().split())
    t.append(a)
    p.append(b)

cnt = 1
# print(t)
# print(p)
res = 0
if t[n-1] == 1:
    d[n-1] = p[n-1]

for i in range(n-1,-1,-1):
    if t[i] + i > n:
        d[i] = d[i + 1]
    else:
        d[i] = max(d[i + t[i]] + p[i], d[i + 1])
print(d[0])