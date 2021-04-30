import itertools
n, m = map(int,input().split())
strm = str(m)
arr = []
cnt = 0
def gum(a):
    if len(a) == len(strm) + 1:
        return
    a4 = a + '4'
    arr.append(a4)
    a7 = a + '7'
    arr.append(a7)
    gum(a4)
    gum(a7)
    return

gum('')
for i in arr:
    if int(i) >= n and int(i) <= m:
        cnt += 1
print(cnt)