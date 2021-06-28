n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

start = arr[1] - arr[0]
end = arr[-1] - arr[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    value = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] >= value + mid:
            value = arr[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)