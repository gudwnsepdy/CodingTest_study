from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
maxValue = 0
all = combinations(arr, 3)
for i in all:
    a = sum(i)
    if a > maxValue and a <= m:
        maxValue = a

print(maxValue)
