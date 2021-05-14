n, m = list(map(int, input().split()))

array = list(map(int, input().split()))
time = []
maxTime = []
for _ in range(m - 1):
    if n % 2 == 1:
        d = (n + 1) // 2
        n -= (n + 1) // 2
    else:
        d = n // 2
        n -= n // 2
    time.append(array[:d])
    del array[:d]

for i in time:
    maxTime.append(sum(i))
maxTime.append(sum(array))
print(array)
print(max(maxTime))