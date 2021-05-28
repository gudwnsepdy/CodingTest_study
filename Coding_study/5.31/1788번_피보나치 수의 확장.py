n = int(input())

flag = 0

if n > 0:
    flag = 1
elif n < 0:
    flag = -1


dp = [0, 1]

for i in range(2, abs(n) + 1):
    dp.append((dp[-1] + dp[-2]) % 1000000000)

if flag == -1:
    if (-n) % 2 != 0:
        flag *= -1

print(flag)
print(dp[abs(n)])