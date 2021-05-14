from collections import deque

def solution(s):
    cnt = 0
    for i in range(len(s)):
        n = deque(s)
        n.rotate(i)
        n = "".join(list(n))
        while 1:
            tmp = n
            n = n.replace("()", "")
            n = n.replace("[]", "")
            n = n.replace("{}", "")
            if tmp == n:
                break
        if len(n) == 0:
            cnt +=1
    return cnt