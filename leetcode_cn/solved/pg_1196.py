from typing import List


class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0
        w = 0
        for i in arr:
            w += i
            ans += 1
            if w > 5000:
                return ans - 1
                break
        return ans
