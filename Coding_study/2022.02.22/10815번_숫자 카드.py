n = int(input())
arr = list(map(int, input().split()))
t = int(input())
test = list(map(int, input().split()))

d = dict()

for i in arr:
    d[i] = 1
res = []
for i in test:
    try:
        res.append(d[i])
    except:
        res.append(0)
print(*res)