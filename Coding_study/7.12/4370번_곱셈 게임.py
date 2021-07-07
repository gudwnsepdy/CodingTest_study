target = int(input())
flag = True
def gob(num, cnt):
    global target, flag
    if num >= target and flag:
        flag = False
        # print(cnt)
        if cnt % 2 == 0:
            print("Baekjoon wins.")
        else:
            print("Donghyuk wins.")
        return cnt
    if flag:
        gob(num * 2, cnt + 1)
        gob(num * 9, cnt + 1)

gob(1, 0)