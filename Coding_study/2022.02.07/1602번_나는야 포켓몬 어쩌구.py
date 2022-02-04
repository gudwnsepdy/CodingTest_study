import sys



n, m = map(int, sys.stdin.readline().split())

d = dict()

for i in range(n):
    a = str(sys.stdin.readline().strip())
    d[i + 1] = a
    d[a] = str(i + 1)

# print(d)
# print(d2)
for i in range(m):
    cmd = input()
    try:
        cmd = int(cmd)
        cmd += 1
        print(d[cmd - 1])
    except:
        print(d[cmd])