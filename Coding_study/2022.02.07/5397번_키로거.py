t = int(input())

for _ in range(t):
    cursor = 0
    s = str(input())
    res = []
    for c in s:
        if c == "<":
            cursor -= 1
            if cursor < 0:
                cursor = 0
        elif c == ">":
            if cursor < len(res):
                cursor += 1
        elif c == "-":
            if cursor == 0:
                continue
            # del res[cursor - 1]
            res = res[:cursor - 1] + res[cursor:]
            cursor -= 1
        else:
            # res.append(c)
            res = res[:cursor] + [c] + res[cursor:]
            if cursor < len(res):
                cursor += 1
    for i in res:
        print(i, end="")
    print()