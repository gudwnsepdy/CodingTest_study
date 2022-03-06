n, l = map(int, input().split())
leak = list(map(int, input().split()))

pipe = [0 for i in range(max(leak))]

for i in leak:
    pipe[i - 1] = 1


cnt = 0
# print(pipe)
for i in range(len(pipe)):

    if pipe[i]:
        cnt += 1
        for k in range(l):
            try:
                pipe[i + k] = 0
            except:
                break

print(cnt)
