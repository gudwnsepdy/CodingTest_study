n = int(input())
arr = []
for i in range(n):
    arr.append(str(input()))

def con_2(s):
    sum = 0
    for i in range(len(s)):
        try:
            sum += int(s[i])
            # print(int(s[i]))
        except:
            continue
    return sum

arr = sorted(arr, key=lambda x: (len(x), con_2(x), x ))
for i in arr:
    print(i)