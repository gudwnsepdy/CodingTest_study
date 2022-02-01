n = int(input())
l = [0]
d = [0 for _ in range(n+1)]
for _ in range(n):
    l.append(int(input()))
d[1] = l[1]
for i in range(n + 1):
    if d[i-1] == d[i-2]:
        d[i] = max((l[i] + d[i-1]), (l[i] + d[i-2]))
    else:
        if i < 3:
            d[i] = max((l[i] + d[i - 1]), (l[i] + d[i - 2]))
        else:
            d[i] = d[i-2] + l[i]

print(d)
print(d[-1])