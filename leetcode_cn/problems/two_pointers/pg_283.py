from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low_speed_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[low_speed_pointer] = nums[i]
                if i != low_speed_pointer:
                    nums[i] = 0
                low_speed_pointer += 1
