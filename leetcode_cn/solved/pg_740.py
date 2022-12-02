from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        sum_nums = [0] * (max_num + 1)
        for num in nums:
            sum_nums[num] += num

        dp = [0] * (max_num + 1)
        dp[0] = sum_nums[0]
        dp[1] = max(sum_nums[0], sum_nums[1])
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + sum_nums[i])
        return dp[-1]
