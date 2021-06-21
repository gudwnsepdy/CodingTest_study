import copy
def up(s):
    s1 = s[0].upper()
    s2 = s[1].upper()
    if ord(s1) < 65 or ord(s1) > 90:
        return
    if ord(s2) < 65 or ord(s2) > 90:
        return
    return s.upper()


def solution(str1, str2):
    answer = 0
    union = []
    new_str1 = []
    new_str2 = []
    inter = []

    for i in range(len(str1) - 1):
        a = up(str1[i] + str1[i + 1])
        # print("1",a)
        if a == None:
            continue
        new_str1.append(a)
        # inter.append(a)
    for i in range(len(str2) - 1):
        # print("2",a)
        a = up(str2[i] + str2[i + 1])

        if a == None:
            continue
        new_str2.append(a)
        # inter.append(a)
    nstr1 = copy.deepcopy(new_str1)
    nstr2 = copy.deepcopy(new_str2)

    for i in nstr1:
        if i in nstr2:
            nstr2.remove(i)
            inter.append(i)
        else:
            inter.append(i)
    for i in nstr2:
        if i in nstr1:
            nstr1.remove(i)
            inter.append(i)
        else:
            inter.append(i)

    # inter = new_str1 + new_str2
    # print(new_str1, new_str2)
    for i in new_str1:
        if i in new_str2:
            union.append(i)
            new_str2.remove(i)
    for i in union:
        new_str1.remove(i)
    # print(new_str1)
    for i in new_str2:
        if i in new_str1:
            union.append(i)
    # union = set(union)
    print(union,inter)
    # for i in union:
    #     inter.remove(i)
    if len(union) == 0:
        return 65536
    else:

        answer = int((len(union) / len(inter)) * 65536)
        # answer = int((2 / 3) * 65536)

    return answer

print(solution(	"FRANCE", "french"))