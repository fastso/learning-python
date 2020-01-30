from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        diff = sum([abs(nums[i] - nums[i + 1]) for i in range(n - 1)])
        ans = diff

        a = max([min(nums[i], nums[i - 1]) for i in range(1, len(nums))])
        b = min([max(nums[i], nums[i - 1]) for i in range(1, len(nums))])
        d = 0
        for i in range(1, len(nums)):
            d = max(d, abs(nums[i] - nums[0]) - abs(nums[i - 1] - nums[i]))
            d = max(d, abs(nums[i - 1] - nums[-1]) - abs(nums[i] - nums[i - 1]))
        return diff + max(2 * a - 2 * b, d)
