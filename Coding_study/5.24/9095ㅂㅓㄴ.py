d =[0 for i in range(11)]

d[0] = 0
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(11):
    if i == 0 or i == 1 or i == 2 or i == 3:
        continue
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    



t = int(input())

for i in range(t):
    n = int(input())
    print(d[n])