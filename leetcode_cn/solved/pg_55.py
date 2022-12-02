from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_max = 0
        for i in range(len(nums)):
            if i <= right_max:
                right_max = max(right_max, i + nums[i])
                if right_max >= len(nums) - 1:
                    return True
        return False
