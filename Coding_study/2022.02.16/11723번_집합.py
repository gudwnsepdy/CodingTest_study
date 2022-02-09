import sys
# input = sys.stdin.readline()

n = sys.stdin.readline()

n = int(n)
s = set()
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
        s.add(num)
    elif cmd == "remove":
        try:
            s.remove(num)
        except:
            continue
    elif cmd == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif cmd == "all":
        s = set([i for i in range(1, 21)])

    elif cmd == "empty":
        s = set([])
    # print(s)