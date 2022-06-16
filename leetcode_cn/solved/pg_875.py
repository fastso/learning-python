import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(k: int) -> bool:
            ans = 0
            for pile in piles:
                ans += math.ceil(pile / k)

            return ans <= h

        left = 1
        right = 10 ** 9

        while left < right:
            mid = (left + right) >> 1
            if not can_eat(mid):
                left = mid + 1
            else:
                right = mid
        return left
