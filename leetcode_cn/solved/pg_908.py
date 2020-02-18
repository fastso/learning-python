from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A.sort()
        ans = abs(A[0] - A[-1]) - 2 * K
        if ans < 0:
            ans = 0
        return ans
