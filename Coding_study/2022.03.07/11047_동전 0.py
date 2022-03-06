n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = arr[::-1]

cnt = 0

for i in arr:
    if not k:
        break
    if i <= k:
        a, b = divmod(k, i)
        k = b
        cnt += a
print(cnt)

