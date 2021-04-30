p = str(input())
flag = False
while (1):
    a = p.replace("PPAP", "P")
    # print(a, p)
    if a == "P":
        flag = True
        break
    if a == p:
        flag = False
        break
    p = a

if flag:
    print("PPAP")
else:
    print("NP")