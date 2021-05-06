from itertools import permutations
def solution(expression):
    answerlist = []
    answer = 0
    symbol = ["*","-","+"]
    all = permutations(symbol)
    for each in all:

        f = each[0]
        new = list(map(str, expression.split(f)))
        print(new)
        new2 =[]
        s = each[1]
        for i in new:
            new2.append(list(map(str, i.split(s))))
        print(new2)

        for i in range(len(new2)):
            for j in range(len(new2[i])):
                new2[i][j] = str(eval(new2[i][j]))

        print(new2)
        for i in range(len(new2)):
            new2[i] = "("+str(eval(s.join(new2[i])))+")"
        print(new2)
        exp = f.join(new2)
        print(exp)
        answerlist.append(abs(eval(exp)))
    return max(answerlist)

print(solution("100-200*300-500+20"))