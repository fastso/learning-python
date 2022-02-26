from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        premin = 10 ** 9
        ans = -1
        for i in range(len(nums)):
            if nums[i] <= premin:
                premin = nums[i]
            else:
                ans = max(ans, nums[i] - premin)
        return ans
