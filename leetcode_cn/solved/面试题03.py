from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            else:
                s.add(n)
