first = str(input())
l = len(first)
if l == 1:
    print(1)
    exit()
half = first[:l // 2]

for i in range(len(first) + 1):
    pal = first + (first[:i])[::-1]
    # print(pal)

    if pal[:len(pal)//2] == pal[len(pal)//2:][::-1]:
        print(len(pal))
        exit()