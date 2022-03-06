s = str(input())

l = len(s)

arr = []
# for i in range(l):
#     for j in range(l):
#         if not (i and j):
#             continue
#         arr.append(s[i:j])

for i in range(l):
        arr.append(s[i:])

arr.sort()
for i in arr:
    print(i)
