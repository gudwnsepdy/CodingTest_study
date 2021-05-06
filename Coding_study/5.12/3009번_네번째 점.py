xarr = []
yarr = []
for _ in range(3):
    a, b = map(int,input().split())
    xarr.append(a)
    yarr.append(b)
result=[]
for i in xarr:
    if xarr.count(i) == 1:
        result.append(i)
        break
for i in yarr:
    if yarr.count(i) == 1:
        result.append(i)
        break

for i in result:
    print(i, end=" ")