from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        vis = [False] * n
        for i in range(n):
            cnt = 0
            while not vis[i]:
                vis[i] = True
                i = nums[i]
                cnt += 1
            ans = max(ans, cnt)
        return ans
