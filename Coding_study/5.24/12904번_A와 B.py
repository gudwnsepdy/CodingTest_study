first = str(input())
second = str(input())

arr = [second]
dp = [[] for i in range(len(second))]

flag = True
cnt = 0
dp[0] = [second]
while(flag):
    # print(dp)
    cnt += 1
    for i in dp[cnt - 1]:
        if i[-1] == "A":
            dp[cnt].append(i[:-1])
        if i[-1] == "B":
            i = i[:-1]
            i = i[::-1]
            dp[cnt].append(i)

    if len(dp[cnt][0]) == 1:
        break
# print(dp)

for i in dp:
    if first in i:
        print(1)
        exit()
print(0)