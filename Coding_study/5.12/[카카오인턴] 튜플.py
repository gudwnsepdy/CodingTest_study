def solution(s):
    s = list(s)
    del s[-1]
    del s[-1]
    del s[0]
    del s[0]
    arr =[]

    s = "".join(s)
    s = list(map(str,s.split('},{')))

    for i in range(len(s)):
        s[i] = list(map(int,s[i].split(",")))

    s.sort(key= lambda x:len(x))
    # print(s)

    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in arr:
                arr.append(s[i][j])
    # print(arr)
    return arr


solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")