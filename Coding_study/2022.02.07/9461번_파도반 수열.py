t = int(input())
arr = [0 for i in range(101)]

arr[:8] = [1, 1, 1, 2, 2, 3, 4, 5]

for i in range(8, 101):
    arr[i] = arr[i - 1] + arr[i - 5]

for _ in range(t):
    i = int(input())
    print(arr[i-1])