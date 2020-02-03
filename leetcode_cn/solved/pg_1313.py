from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = list()
        i = 0
        while i < len(nums):
            n = nums[i]
            for j in range(n):
                ans.append(nums[i + 1])
            i += 2
        return ans
