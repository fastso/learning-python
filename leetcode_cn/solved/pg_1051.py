from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sort = heights[:]
        heights_sort.sort()

        ans = 0
        for i in range(len(heights)):
            if heights_sort[i] != heights[i]:
                ans += 1
        return ans
