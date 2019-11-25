from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hash_table:
                return [hash_table.get(target - nums[i]), i]
            else:
                hash_table.setdefault(nums[i], i)
