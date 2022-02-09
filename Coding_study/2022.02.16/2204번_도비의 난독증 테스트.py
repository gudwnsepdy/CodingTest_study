while 1:
    t = int(input())
    if not t:
        exit()
    arr = []
    for i in range(t):
        # arr.append(input().lower())
        arr.append(input())
    arr.sort(key=str.lower)
    print(arr[0])