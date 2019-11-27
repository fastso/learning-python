from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new_len = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[new_len] = nums[i]
                new_len += 1
        return new_len
