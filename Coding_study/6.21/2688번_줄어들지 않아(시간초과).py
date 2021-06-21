t = int(input())

def plus(n, num, idx):
    global flag
    for i in range(int(str(num)[-1]), 10):
        if len(str(num * 10 + i)) <= n and (num * 10 + 1) not in arr[idx]:
            flag = True
            arr[idx + 1].append(num * 10 + i)


for _ in range(t):
    arr = [[0,1,2,3,4,5,6,7,8,9]]
    n = int(input())
    idx = -1
    while 1:
        idx += 1
        flag = False

        arr.append([])
        # print(idx, arr)
        for i in arr[idx]:
            plus(n, i, idx)
        for i in range(len(arr)):
            print(arr[i])
        if not flag:
            break
    new = []
    for i in arr:
        new += i
    print(len(new))