class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        y_n = customers.count('Y')
        dp = [0] * (n + 1)
        dp[0] = y_n
        for i in range(1, n + 1):
            if customers[i - 1] == 'Y':
                dp[i] = dp[i - 1] - 1
            else:
                dp[i] = dp[i - 1] + 1
        dp_min = min(dp)
        dp_min_index = dp.index(dp_min)
        return dp_min_index
