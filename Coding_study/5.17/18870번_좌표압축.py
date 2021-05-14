n = int(input())
arr = list(map(int,input().split()))

narr = arr[:]
arr = set(arr)
arr = list(arr)
arr.sort()

dic = {arr[i] : i for i in range(len(arr))}