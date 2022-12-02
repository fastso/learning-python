from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0] = nums[0]
        dp2[0] = nums[0]
        for i in range(1, len(nums)):
            dp1[i] = max(dp1[i - 1] + nums[i], nums[i])
            dp2[i] = min(dp2[i - 1] + nums[i], nums[i])
        return max(max(dp1), sum(nums) - min(dp2))