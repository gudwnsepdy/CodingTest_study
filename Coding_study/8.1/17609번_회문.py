t = int(input())
def check(s):
    forward = s[:len(s) // 2]
    back = s[len(forward):][::-1]

    if forward == back:
        return True
    else:
        return False

for _ in range(t):
    n = list(input())
    if check(n):
        print(0)
        continue

    flag = False
    for i in range(len(n)):
        tmp = n[:]
        del tmp[i]
        s = "".join(tmp)
        if check(s):
            flag = True
            break
    if flag:
        print(1)
    else:
        print(2)