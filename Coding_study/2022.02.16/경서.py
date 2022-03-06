import sys

front = list(sys.stdin.readline())
back = []

m = int(sys.stdin.readline())

for _ in range(m):
    cmd = sys.stdin.readline().split()
    if len(front)>0 and cmd[0]=='L':
        back.append(front[len(front)-1])
        front.pop()
    elif len(back)>0 and cmd[0]=='D':
        front.append(back[len(back)-1])
        back.pop()
    elif len(front)>0 and cmd[0]=='B':
        front.pop()
    elif cmd[0]=='P':
        front.append(cmd[1])

print(''.join(front+list(reversed(back))))