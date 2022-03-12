from itertools import permutations
def solution(money, costs):
    worth = [1, 5, 10, 50, 100, 500]
    answer = 0
    all = list(permutations(costs, 6))

    res = []
    cnt = 0
    for case in all:
        total = 0
        new_money = money
        cnt += 1
        case = list(case)
        new_worth = [0, 0, 0, 0, 0, 0]
        for i in range(len(case)):
            new_worth[case.index(costs[i])] = worth[i]

        for i in range(6):
            if case[i] <= new_money:
                a, b = divmod(new_money, new_worth[i])
                new_money = b
                total += a * case[i]
        res.append(total)
    answer = min(res)
    return answer

print(solution(4578, [1, 4, 99, 35, 50, 1000]))