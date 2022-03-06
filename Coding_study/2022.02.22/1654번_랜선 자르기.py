n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

start = 1
end = max(arr)
f = 0
res = 0
while start <= end:
    mid = (start + end ) // 2

    res = 0

    for i in arr:
        res += i // mid

    if res < k:
        end = mid - 1
    else:

        start = mid + 1
print(end)
