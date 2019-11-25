from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

                    print('---------------------------')
                    print('Loop k=' + str(k) + ' left=' + str(left) + ' i=' + str(i))
                    print('Nums Interval:' + str(nums[left:right + 1]))
                    print('dp[' + str(left) + '][' + str(right) + '] = max(' + 'dp[' + str(left) + '][' + str(
                        right) + '], nums[' + str(left) + '] * nums[' + str(i) + '] * nums[' + str(
                        right) + '] + dp[' + str(left) + '][' + str(i) + '] + dp[' + str(i) + '][' + str(right) + '])')
                    print('---------------------------')
                    for x in dp:
                        print(*x)
        return dp[0][n - 1]
