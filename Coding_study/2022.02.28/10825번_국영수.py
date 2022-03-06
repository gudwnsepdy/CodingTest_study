n = int(input())
arr = []
for i in range(n):
    a, b, c, d = map(str, input().split())
    arr.append([a, int(b), int(c), int(d)])

arr = sorted(arr, key=lambda x :(-x[1],x[2],-x[3],x[0]))

for i in range(n):
    print(arr[i][0])