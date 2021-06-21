def solution(n):
    ans = 0

    dp = [i for i in range(n + 1)]

    for i in range(1, n + 1):
        # if i % 2 == 0:
        #     dp[i] = min(dp[i - 1] + 1, dp[i // 2])
        # else:
        #     dp[i] = dp[i - 1] + 1
        dp[i] = min(dp[i], dp[i - 1] + 1)
        if i * 2 <= n + 1:
            dp[i * 2] = dp[i]
    # print(dp)
    return dp[-1]


print(solution(6))