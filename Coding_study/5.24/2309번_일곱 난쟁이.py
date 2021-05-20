from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(input()))

allCase = combinations(arr, 7)

for i in allCase:
    if sum(i) == 100:
        i = list(i)
        i.sort()
        for j in i:
            print(j)
        exit()