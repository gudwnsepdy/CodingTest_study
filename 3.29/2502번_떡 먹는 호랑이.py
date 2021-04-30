n, m = map(int, input().split())

d = [[0,0] for _ in range(30)]

for i in range(30):
    if i == 0:
        d[i] = [1,0]
    elif i == 1:
        d[i] = [0,1]
    else:
        d[i][0] = d[i-1][0] + d[i - 2][0]
        d[i][1] = d[i - 1][1] + d[i - 2][1]

# print(d[5])

for i in range(100001):
    for j in range(100001):
        if (d[n - 1][0] * i) + (d[n - 1][1] * j) == m:
            print(i)
            print(j)
            exit()
