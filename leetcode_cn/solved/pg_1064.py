from typing import List


class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for k, v in enumerate(A):
            if k == v:
                return k
        return -1
