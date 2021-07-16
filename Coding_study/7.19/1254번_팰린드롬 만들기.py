first = str(input())
l = len(first)
if l == 1:
    print(1)
    exit()
elif l == 2:
    if first[0] == first[1]:
        print(2)
        exit()
half = first[:l // 2]

for i in range(len(first) + 1):
    pal = first + (first[:i])[::-1]

    forward = pal[:len(pal)//2]
    back = pal[len(forward):][::-1]
    if len(forward) != len(back):
        back = back[:-1]

    if back == forward:
        print(len(pal))
        exit()