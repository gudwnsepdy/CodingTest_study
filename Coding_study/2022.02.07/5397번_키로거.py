from collections import deque
t = int(input())
right = deque()
left = deque()

for _ in range(t):
    right = deque()
    left = deque()

    s = str(input())

    for c in s:
        if c == "<":
            if left:
                right.appendleft(left.pop())
        elif c == ">":
            if right:
                left.append(right.popleft())
        elif c == "-":
            if left:
                left.pop()
        else:
            left.append(c)

    res = left + right

    for i in res:
        print(i, end="")
    print()