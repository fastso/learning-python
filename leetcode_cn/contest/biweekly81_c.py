from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefixes = set([num >> i for num in nums])
            ans += any(ans ^ 1 ^ p in prefixes for p in prefixes)
        return ans