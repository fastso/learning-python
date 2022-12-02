from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, start, end = 0, 0, 1

        while end < len(nums):
            max_pos = 0
            for i in range(start, end):
                max_pos = max(max_pos, i + nums[i])
                print(start, end, max_pos)
            start = end
            end = max_pos + 1
            ans += 1
        return ans



