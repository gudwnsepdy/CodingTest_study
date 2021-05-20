from itertools import combinations

arr = []
i = 0
while i < 9:
    a = int(input())
    arr.append(a)
    i += 1
perarr = list(combinations(arr, 7))
i = 0
for a in perarr:
    if sum(a) == 100:
        break
    i += 1
print(perarr[i])
perarr = list(perarr[i])
sperarr = perarr.sorted()
for b in sperarr:
    print(b)