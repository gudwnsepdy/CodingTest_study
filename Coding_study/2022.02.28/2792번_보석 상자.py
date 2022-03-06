import sys

input = sys.stdin.readline
n, m = map(int, input().split())
colors = []
for i in range(m):
    colors.append(int(input()))

start = 1
end = max(colors)
res = 9999999999
while start <= end:
    mid = (start + end ) // 2

    std = 0

    for c in colors:
        if c % mid == 0:
            std += c // mid
        else:
            std += c // mid + 1


    if std > n: # 조건을 만족하지 않을 때
        # end = mid - 1
        start = mid + 1

        # print(mid)
    else: # 못받는 학생이 잇음
        res = min(res, mid)
        # start = mid + 1
        end = mid - 1

print(res)
