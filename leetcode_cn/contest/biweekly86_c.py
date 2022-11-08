from typing import List


class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j >= cols:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - n] + sum(mat[i - 1]))
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][cols]