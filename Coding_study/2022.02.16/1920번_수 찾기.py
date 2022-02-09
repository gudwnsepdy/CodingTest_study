n = int(input())
arr = list(map(int, input().split()))
t = int(input())
test = list(map(int, input().split()))

d = dict()

for i in arr:
    d[i] = 1

for i in test:
    try:
        print(d[i])
    except:
        print(0)