n = int(input())
m = int(input())
broken = list(map(int, input().split()))

def remote(pm,n):
    cnt = 0
    flag = True
    while(flag):
        iflag = True
        for i in broken:
            if str(i) in str(n):
                n += pm
                cnt += 1
                iflag = False
                break
        if iflag:
            break
    return cnt

only_up_down = n - 100
minus = remote(-1, n)
plus = remote(1, n)
cnt = min(minus, plus, only_up_down)

if(only_up_down <= minus and only_up_down <= plus):
    print(only_up_down)
else:
    print(cnt + len(str(n)))