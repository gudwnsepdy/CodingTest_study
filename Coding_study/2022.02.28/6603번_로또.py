from itertools import combinations
while 1:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    arr = arr[1:]
    arr.sort()
    # arr = set(arr)
    res = set(list(combinations(arr,6)))
    res = sorted(list(res))
    for i in res:
        i = sorted(i)
        print(i[0],i[1],i[2],i[3],i[4],i[5])
    print()