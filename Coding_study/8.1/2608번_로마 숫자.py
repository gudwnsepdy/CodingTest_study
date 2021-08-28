a = str(input())
b = str(input())
res = 0

res += a.count("IV") * 4 + b.count("IV") * 4
a = a.replace("IV", "")
b = b.replace("IV", "")
res += a.count("IX") * 9 + b.count("IX") * 9
a = a.replace("IX", "")
b = b.replace("IX", "")
res += a.count("XL") * 40 + b.count("XL") * 40
a = a.replace("XL", "")
b = b.replace("XL", "")
res += a.count("XC") * 90 + b.count("XC") * 90
a = a.replace("XC", "")
b = b.replace("XC", "")
res += a.count("CD") * 400 + b.count("CD") * 400
a = a.replace("CD", "")
b = b.replace("CD", "")
res += a.count("CM") * 900 + b.count("CM") * 900
a = a.replace("CM", "")
b = b.replace("CM", "")
res += a.count("I") + b.count("I")
res += a.count("V") * 5 + b.count("V") * 5
res += a.count("X") * 10 + b.count("X") * 10
res += a.count("L") * 50 + b.count("L") * 50
res += a.count("C") * 100 + b.count("C") * 100
res += a.count("D") * 500 + b.count("D") * 500
res += a.count("M") * 1000 + b.count("M") * 1000
print(res)
str_res = []
for i in str(res):
    str_res.append(int(i))
ans = ""
if len(str_res) == 4:
    a = str_res.pop(0)
    # 1000자리
    for i in range(a):
        ans += "M"

# 100자리

if len(str_res) == 3:
    b = str_res.pop(0)
    if b == 9:
        ans += "CM"
    elif b == 4:
        ans += "CD"
    elif b == 5:
        ans += "D"
    else:
        if b >5:
            ans += "D"
            for i in range(b - 5):
                ans += "C"
        else:
            for i in range(b):
                ans += "C"

if len(str_res) == 2:
    c = str_res.pop(0)
    # 10자리
    if c == 9:
        ans += "XC"
    elif c == 4:
        ans += "XL"
    elif c == 5:
        ans += "L"
    else:
        if c >5:
            ans += "L"
            for i in range(c - 5):
                ans += "X"
        else:
            for i in range(c):
                ans += "X"

# 1자리
d = str_res.pop(0)
if d == 9:
    ans += "IX"
elif d == 5:
    ans += "V"
elif d > 5:
    ans += "V"
    for i in range(d - 5):
        ans += "I"
elif d == 4:
    ans += "IV"
else:
    for i in range(d):
        ans += "I"

print(ans)