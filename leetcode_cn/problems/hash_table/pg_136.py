from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = set()
        for i in nums:
            if i in ans:
                ans.remove(i)
            else:
                ans.add(i)
        return ans.pop()
