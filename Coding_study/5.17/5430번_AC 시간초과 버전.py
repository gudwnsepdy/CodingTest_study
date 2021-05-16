t = int(input())
for _ in range(t):
    p = list(input().strip())
    n = int(input())

    arr = str(input())
    if n == 0:
        print("error")
        continue
    arr = arr.replace("[", "")
    arr = arr.replace("]", "")

    arr = list(map(int,arr.split(",")))
    flag = True

    for i in p:
        if i == 'R':
            arr.reverse()
        if i == "D":
            if len(arr) == 0:
                print("error")
                flag = False
                break
            arr = arr[1:]
    if not flag:
        continue
    if len(arr) == 0 and flag:
        print("error")
        continue
    print(arr)