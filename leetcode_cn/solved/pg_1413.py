from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        sum = 0
        for i in nums:
            sum += i
            if sum < 0:
                ans = max(ans, -sum + 1)
        return ans