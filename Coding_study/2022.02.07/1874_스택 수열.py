from collections import deque
n = int(input())
arr = []
for i in  range(n):
    arr.append(int(input()))
q = deque()
arr_copy = arr[::]

cnt = 1
res = []
while 1:
    if cnt == arr[0]:
        res.append("+")
        res.append("-")
        cnt += 1
        arr = arr[1:]
        if arr == []:
            break

    else:
        break
q.append(cnt)
res.append("+")
arr2 = []
if arr == []:
    for i in res:
        print(i)
    exit()
while(q):
    if cnt == 10:
        break
    t = q.pop()
    if arr[0] == t:
        res.append("-")
        arr = arr[1:]
        arr2.append(t)
    else:
        q.append(t)
        cnt += 1
        q.append(cnt)
        res.append("+")

# print(arr2)
# print(arr_copy)
if arr_copy == arr2:
    for i in res:
        print(i)
else:
    print("NO")