import sys
# input = sys.stdin.readline()

n = sys.stdin.readline()

n = int(n)
s = [0 for i in range(20)]
for i in range(n):
    command = sys.stdin.readline().rstrip()
    try:
        cmd, num = command.split()
        num = int(num)
        # print(cmd)
    except:
        cmd = command
        # print(cmd)
    if cmd == "add":
        s[num - 1] = 1
    elif cmd == "remove":
        s[num - 1] = 0
    elif cmd == "check":
        if s[num - 1]:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if s[num - 1]:
            s[num - 1] = 0
        else:
            s[num - 1] = 1
    elif cmd == "all":
        s = [1 for i in range(20)]

    elif cmd == "empty":
        s = [0 for i in range(20)]
    # print(s)