from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        min_num = nums[-1]
        for i in range(len(nums) - 2, 1, -1):
            if nums[i] > min_num:
                return False
            min_num = min(min_num, nums[i + 1])
        return True

