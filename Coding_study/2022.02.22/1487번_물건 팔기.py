n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr = sorted(arr, key=lambda x: (x[0], x[1]))
res = 0
final_price = 0
for i in range(n):
    price = arr[i][0]
    total = 0
    for j in range(n):
        if arr[j][0] >= price:
            # print(price, arr[j][0])
            if price - arr[j][1] > 0:
                total += price
                total -= arr[j][1]
    # print(total)
    if total > res:
        res = total
        final_price = price

print(final_price)