def solution(money, costs):
    answer = 0
    worth = [1, 5, 10, 50, 100, 500]
    # origin_cost = costs[::]
    # print(origin_cost)
    def cost_effective(m):
        w = costs[worth.index(m)]
        return w - m

    new_worth = sorted(worth, key=lambda x : cost_effective(x))

    new_cost = [0,0,0,0,0,0]
    for i in range(len(new_worth)):
        new_cost[new_worth.index(worth[i])] = costs[i]

    # costs = sorted(costs, key=lambda x : cost_effective(x))
    print(new_worth)
    print(new_cost)

    for i in range(len(worth)):
        if new_worth[i] <= money:
            print(new_worth[i])
            a, b = divmod(money, new_worth[i])
            money = b
            answer += a * new_cost[i]
    return answer

print(solution(1999, [2, 11, 20, 100, 200, 600]))