t = int(input())
for tn in range(t):

    flag = True
    sign = 1
    plus = 0
    minus = 0


    p = list(input().strip())
    n = int(input())
    arr = str(input())
    # if n == 0:
    #     print("[]")
    #     continue
    arr = arr.replace("[", "")
    arr = arr.replace("]", "")
    if n != 0:
        arr = list(map(int,arr.split(",")))

    if n == 0:
        if "D" in p:
            print("error")
            continue
        else:
            print("[]")
            continue
    for i in p:
        if i == 'R':
            sign *= -1
        if i == "D":
            if sign == 1:
                plus += 1
                if plus + minus > n:
                    print("error")
                    flag = False
                    break
            else:
                minus += 1
                if plus + minus > n:
                    print("error")
                    flag = False
                    break

    if not flag:
        continue


    minus *= -1
    if sign == -1:
        # arr = arr.reverse()
        if plus == 0 and minus == 0:
            arr.reverse()
            arr = str(arr).replace(" ","")
            print(arr)
        elif plus == 0:
            arr = arr[:minus]
            arr.reverse()
            arr = str(arr).replace(" ", "")
            print(arr)
        elif minus == 0:
            arr = arr[plus:]
            arr.reverse()
            arr = str(arr).replace(" ", "")
            print(arr)
        else:
            arr = arr[plus:minus]
            arr.reverse()
            arr = str(arr).replace(" ", "")
            print(arr)
    else:
        if plus == 0 and minus == 0:
            arr = str(arr).replace(" ", "")
            print(arr)
        elif plus == 0:
            arr = arr[:minus]
            arr = str(arr).replace(" ", "")
            print(arr)
        elif minus == 0:
            arr = arr[plus:]
            arr = str(arr).replace(" ", "")
            print(arr)
        else:
            arr = arr[plus:minus]
            arr = str(arr).replace(" ", "")
            print(arr)