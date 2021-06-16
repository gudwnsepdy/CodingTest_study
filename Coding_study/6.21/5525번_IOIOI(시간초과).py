n = int(input())
s = int(input())
string = list(input().strip())

p = ["I"]

for i in range(n):
    p += ["O", "I"]
    # if p.count("O") == n:
    #     break

# print(p)
# print(string)
cnt = 0
part = string[:3]
# del string[:3]
string = string[3:]
if part == p:
    cnt += 1
for i in range(s - n - 2):
    # del part[0]
    part = part[1:]
    part += string[0]
    # print(part)
    # del string[0]
    string = string[1:]
    if part == p:
        cnt += 1

print(cnt)