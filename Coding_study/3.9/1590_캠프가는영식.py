def bus(t, start, term, num):
    time_table = []

    time_table.append(start)

    for i in range(1, num):
        # print(i - 1)
        i * term
        if start + i * term >= t:
            time_table.append(start + i * term)
            break

    if time_table[0] < t:
        del time_table[0]

    # print(time_table)
    if not time_table:
        return None
    else:
        return time_table[0] - t

n, t = map(int, input().split())

pos = []

for _ in range(n):
    start, term, num = map(int, input().split())
    data = bus(t, start, term, num)

    if data == None:
        continue
    else:
        pos.append(data)



if not pos:
    print(-1)
else:
    print(min(pos))
