from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = nums.count(target)
        if count > len(nums) / 2:
            return True
        else:
            return False
