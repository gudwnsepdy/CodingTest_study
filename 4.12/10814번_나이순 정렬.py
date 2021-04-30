n = int(input())

arr = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    arr.append([age, i,name])


arr = sorted(arr, key = lambda x : (x[0], x[1]))

for i in arr:
    print(i[0], i[2])