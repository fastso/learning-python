class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        dp = [[0] * (budget + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, budget + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= chargeTimes[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - chargeTimes[i - 1]] + runningCosts[i - 1])
        return dp[n][budget]
