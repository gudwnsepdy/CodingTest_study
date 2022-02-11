from itertools import combinations

n, m = map(int, input().split())
ice = [i for i in range(1,n + 1)]
arr = [[0 for j in range(n)] for i in range(n)]

# print(arr)
for i in range(m):
    a, b = map(int, input().split())
    # arr.append((a, b))
    arr[a - 1][b - 1] = 1
    arr[b - 1][a - 1] = 1

ice_combi = list(combinations(ice, 3))

cnt = 0

for a, b, c in ice_combi:
    if arr[a - 1][b - 1] or arr[b - 1][c - 1] or arr[a - 1][c - 1]:
        continue
    cnt += 1
    # print(a,b,c)
print(cnt)