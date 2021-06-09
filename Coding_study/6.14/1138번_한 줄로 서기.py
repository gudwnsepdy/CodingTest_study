n = int(input())
arr = list(map(int, input().split()))

line = [0 for _ in range(n)]


# line[arr[0]] = 1
idx = 0
for i in arr:
    # print(line)
    idx += 1
    cnt = 0
    for j in range(n):
        if cnt == i and line[j] == 0:
            line[j] = idx
            cnt = 0
            break
        if line[j] == 0:
            cnt += 1

print(*line)