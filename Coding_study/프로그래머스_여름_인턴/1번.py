def solution(code, day, data):
    answer = []
    tmp = []
    code = "code=" + code
    day = "time=" + day
    for d in data:
        if code in d and day in d:
            price, code, time = d.split()

            priceString, price = price.split("=")
            price = int(price)

            timeString, time = time.split("=")
            time = int(time)
            tmp.append([time,price])

    tmp = sorted(tmp, key= lambda x:x[0])
    for t in tmp:
        answer.append(t[1])
    return answer



print(solution("012345","20190620",["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))