from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        half = n // 2
        remainder = n % 2

        ans = list()
        for i in range(-half, half + 1):
            if not remainder and i == 0:
                continue
            ans.append(i)
        return ans
