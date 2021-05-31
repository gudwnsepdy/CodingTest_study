def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

arr = []

for i in range(m):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x: x[2])

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

# cycle = False
res = 0
for a, b, c in arr:
    if find(parent, a) == find(parent, b):
        continue
    else:
        union(parent, a, b)
        res += c

print(res)