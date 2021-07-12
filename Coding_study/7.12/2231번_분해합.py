target = int(input())

cnt = target - 10 * len(str(target)) if target > 18 else 0

while 1:
    n, a = str(cnt), cnt

    for i in range(len(n)):
        a += int(n[i])
    if a == target:
        print(cnt)
        break
    if cnt > target:
        print(0)
        break
    cnt += 1