n = int(input())

body = []

for _ in range(n):
    x, y = map(int, input().split())
    body.append([x, y, 1, _])

body = sorted(body, key=lambda x : -x[0])
# print(body)
cnt = 0
for i in range(len(body)):
    # cnt = 0
    if body[i][2] != 1:
        continue
    if(i >= 0):
        body[i][2] = body[i - 1][2] + 1
        # body[i][2] += cnt
        cnt = 0
    for j in range(i, len(body)):
        if j + 1 >= len(body):
            break
        if body[j][1] <= body[j + 1][1]:
            body[j + 1][2] = body[j][2]
            cnt += 1
            # print(cnt)
        else:
            body[j + 1][2] = body[j][2] + cnt + 1

result = sorted(body, key=lambda x : x[3])
# print(result)
for each in result:
    print(each[2] - 1, end=' ')