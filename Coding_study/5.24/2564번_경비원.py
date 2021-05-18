n, m = map(int, input().split())

shop_num = int(input())

shops = []

def clock(a,b):
    global n, m
    cnt = 0
    if dong[0] == 1:
        if a == 1:
            if b > dong[1]:
                cnt = b - dong[1]
            else:
                cnt = (n - dong[1]) + (2 * m) + b
        if a == 2:
            cnt = (n - dong[1]) + m + (n - b)
        if a == 3:
            cnt = (n - dong[1]) + m + n + (m - b)
        if a == 4:
            cnt = (n - dong[1]) + b
    elif dong[0] == 2:
        if a == 1:
            cnt = dong[1] + m + b
        if a == 2:
            if b > dong[1]:
                cnt = dong[1] + (2 * m ) + n + (n - b)
            else:
                cnt = dong[1] - b
        if a == 3:
            cnt = dong[1] + (m - b)
        if a == 4:
            cnt = dong[1] + m + n + b
    elif dong[0] == 3:
        if a == 1:
            cnt = dong[1] + b
        if a == 2:
            cnt = dong[1] + n + m + (n - b)
        if a == 3:
            if b > dong[1]:
                cnt = dong[1] + (2 * n) + m + (m - b)
            else:
                cnt = dong[1] - b
        if a == 4:
            cnt = dong[1] + n + b
    else:
        if a == 1:
            cnt = (m - dong[1]) + n + m + b
        if a == 2:
            cnt = (m - dong[1]) + (n - b)
        if a == 3:
            cnt = (m - dong[1]) + n + (m - b)
        if a == 4:
            if b > dong[1]:
                cnt = b - dong[1]
            else:
                cnt = m - dong[1] + 2 * n + m + b
    return cnt

def reverse_clock(a,b):
    global n, m
    cnt = 0
    if dong[0] == 1:
        if a == 1:
            if b > dong[1]:
                cnt = (n - b) + m + n + m + dong[1]
            else:
                cnt = dong[1] - b
        if a == 2:
            cnt = dong[1] + m + b
        if a == 3:
            cnt = dong[1] + b
        if a == 4:
            cnt = dong[1] + n + m + (m - b)
    elif dong[0] == 2:
        if a == 1:
            cnt = (n - dong[1]) + m + (n - b)
        if a == 2:
            if b > dong[1]:
                cnt = b - dong[1]
            else:
                cnt = (n - dong[1]) + 2 * m + n + b
        if a == 3:
            cnt = (n - dong[1]) + n + m + b
        if a == 4:
            cnt = n - dong[1] + m - b
    elif dong[0] == 3:
        if a == 1:
            cnt = m - dong[1] + n + m + (n - b)
        if a == 2:
            cnt = m - dong[1] + b
        if a == 3:
            if b > dong[1]:
                cnt = b - dong[1]
            else:
                cnt = m - dong[1] + n + n + m + b
        if a == 4:
            cnt = m - dong[1] + n + (m - b)
    else:
        if a == 1:
            cnt = dong[1] + (n - b)
        if a == 2:
            cnt = dong[1] + n + m + b
        if a == 3:
            cnt = dong[1] + n + b
        if a == 4:
            if b > dong[1]:
                cnt = dong[1] + n + n + m + (n - b)
            else:
                cnt = dong[1] - b
    return cnt


for i in range(shop_num + 1):
    a, b = map(int, input().split())
    if i <= shop_num:
        shops.append([a,b])
    else:
        dong = [a, b]


dong = shops.pop()
res = 0

for i in shops:
    a, b = i
    res += min(clock(a, b), reverse_clock(a, b))

print(res)


