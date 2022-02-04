n = int(input())
arr = []
for i in range(n):
    arr.append(str(input()))
l = len(arr[0])
res = ""
for i in range(l):
    flag = True
    tmp = arr[0][i]
    for word in arr:
        if word[i] != tmp:
            flag = False
    if flag:
        res += tmp
    else:
        res += "?"

print(res)