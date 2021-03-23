from itertools import combinations

n = int(input())
li = [i for i in range(1,n)]


taste = []

for _ in range(n):
    taste.append(list(map(int, input().split())))

kinds = []
for i in range(1, n+1):
    kinds += list(combinations(taste, i))


result = []
for recipe in kinds:
    sour = 1
    bitter = 0
    for ingredient in recipe:

        sour *= ingredient[0]
        bitter += ingredient[1]

    result.append(abs(sour - bitter))

print(min(result))