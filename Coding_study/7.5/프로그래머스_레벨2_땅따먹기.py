def solution(land):
    answer = 0
    n = len(land)
    dp = [[0, 0, 0, 0] for i in range(n)]

    dp[0] = land[0]
    for i in range(1, n):
        for j in range(4):
            arr = []
            for k in range(4):
                if k != j:
                    arr.append(dp[i-1][k])
            dp[i][j] = max(arr) + land[i][j]

    return max(dp[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
