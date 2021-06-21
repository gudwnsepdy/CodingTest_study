t = int(input())

def plus(n, num, idx):
    global flag
    tmp = int(str(num)[-1])
    for x in range(tmp , 10):
        flag = True
        arr[idx + 1].append(x)

for _ in range(t):
    arr = [[0,1,2,3,4,5,6,7,8,9]]
    
    n = int(input())
    idx = -1
    minus = 0
    while 1:
        idx += 1
        flag = False

        arr.append([])
        # print("************************************************************************************************")
        # print(idx, arr)
        for i in arr[idx]:
            plus(n, i, idx)
        if not flag:
            break
        minus += len(arr[idx])
        print(len(arr[idx]))
        for i in range(len(arr)):
            print(arr[i])
        if idx == n - 2:
            break
    new = []
    for i in arr:
        new += i
    print(len(new) - minus)