def solution(s):
    answer = [0,0]

    while s != "1":
        answer[0] += 1
        n = s.count("0")
        answer[1] += n
        s = s.replace("0", "")
        s = len(s)
        s = str(bin(int(s)))[2:]

    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
