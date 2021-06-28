def cal(e):
    peer = 0
    if e <= 100:
        return e * 2
    elif e >= 101 and e <= 10000:
        return 2 * 100 + 3 * (e - 100)
    elif e >= 10001 and e <= 1000000:
        return 2 * 100 + 3 * 9900 + 5 * (e - 10000)
    elif e > 1000000:
        return 2 * 100 + 3 * 9900 + 5 * (990000) + 7 * (e - 1000000)


def cal2(cost):
    if cost > 1000000:
        return cost * 7 - 2020100
    elif cost > 10000:
        return cost * 5 - 20100
    elif cost > 100:
        return cost * 3 - 100
    else:
        return cost * 2
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    # def cal2(cost):
    #     if use > 1000000:
    #         return use * 7 - 2020100
    #     elif use > 10000:
    #         return use * 5 - 20100
    #     elif use > 100:
    #         return use * 3 - 100
    #     else:
    #         return use * 2
    # print(cal(1000001))
    # print(cal2(1000001))
    # print(cal2(10123))


    start = 0
    end = a
    res = 0

    while(start <= end):

        mid = (start + end) // 2
        # print(mid)
        c = cal2(mid)
        # print(mid, c)
        if c == a:
            res = mid
            break
        if c > a:
            end = mid - 1
        else:
            start = mid + 1
    # print(res)
    start = 0
    end = res
    while(start <= end):

        mid = (start + end) // 2
        # print(mid)
        c = cal2(mid)
        n = cal2(res - mid)

        # print(c, n)
        if n - c == b:
            # res = mid
            print(c)
            break
        if n - c < b:
            end = mid - 1
        else:
            start = mid + 1
