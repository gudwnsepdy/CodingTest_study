n = int(input())

d = [[0, 0] for _ in range(n)]

d[0][0], d[0][1] = 1,1
print(d)
for i in range(1, n):
    print(i)
    d[i] = max(d[i-1][0], d[i- 1][1]) + 1

print(d)