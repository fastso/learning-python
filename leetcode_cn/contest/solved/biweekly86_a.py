from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 2):
            temp1 = sum(nums[i:i + 2])
            for j in range(i + 1, n - 1):
                temp2 = sum(nums[j:j + 2])
                if temp1 == temp2:
                    return True
        return False
