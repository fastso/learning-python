from typing import List


class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_val = float('inf')
        for i in A:
            min_val = min(min_val, i)

        ans = 0
        l = list(str(min_val))
        for c in l:
            ans += int(c)

        if ans % 2:
            return 0
        else:
            return 1
