def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# v, e = map(int, input().split())
n = int(input())
m = int(input())
parent = [0] * (n + 1)


for i in range(1, n + 1):
    parent[i] = i

# print(parent)
for i in range(1,n + 1):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            # print(i, j + 1)
            union_parent(parent, i, j+ 1)


cities = list(map(int, input().split()))

root = parent[cities[0]]
flag = True
for city in cities:
    if root != parent[city]:
        flag = False

if flag:
    print("YES")
else:
    print("NO")




# print(parent)