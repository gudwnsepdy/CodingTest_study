import sys
from collections import deque

s = list(input().strip())
right_list = deque([])
left_list = deque(s)

m = int(input())

for i in range(m):
    command = sys.stdin.readline().rstrip()
    try:
        cmd, d = command.split()
    except:
        cmd = command

    if cmd == "L":
        try:
            right_list.appendleft(left_list.pop())
        except:
            continue
    elif cmd == "D":
        try:
            left_list.append(right_list.popleft())
        except:
            continue
    elif cmd == "B":
        try:
            left_list.pop()
        except:
            continue
    elif cmd == "P":
        left_list.append(d)
    # print(left_list, right_list)

print(''.join(left_list) + ''.join(right_list))
