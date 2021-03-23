import copy
from sys import stdin
n = int(stdin.readline())

arr = list(map(str, stdin.readline().split()))

rank = []
for i in arr:
    if i not in rank:
        rank.append(i)
# rank = list(rank2)
rank.sort()
for el in arr:
    print(list(rank).index(el), end=" ")