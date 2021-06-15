t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    remainder = c % a
    if remainder == 0:
        remainder = a
        mod = c // a
    else:
        mod = c // a + 1
    remainder = str(remainder)




    if len(str(mod)) == 1:
        mod = "0" + str(mod)
    else:
        mod = str(mod)
    print(remainder + mod)
