n = int(input())

d = [ 0 for _ in range(50)]
a = 0

d[0], d[1] = 1, 1

for i in range(2, n + 1):
    d[i] = (d[i-1] + d[i -2] + 1)%1000000007

print(d[n])