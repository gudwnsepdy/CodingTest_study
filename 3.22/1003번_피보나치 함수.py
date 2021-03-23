from sys import stdin
d = [[0,0] for _ in range(100)]


def fibo(x):
    if x == 0:
        d[x][0] = 1
        return d[x]
    if x == 1:
        d[x][1] = 1
        return d[x]
    if d[x] != [0,0]:
        return d[x]

    d[x][0] += fibo(x - 1)[0] + fibo(x - 2)[0]
    d[x][1] += fibo(x - 1)[1] + fibo(x - 2)[1]
    return d[x]
a = []
for _ in range(int(stdin.readline())):
    a.append(int(stdin.readline()))

for i in a:
    print(*fibo(i))