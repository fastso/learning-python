from functools import reduce
from operator import xor
from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        total_with0 = reduce(xor, range(1, len(encoded) + 2))
        total = reduce(xor, encoded[1::2])

        ans = [total_with0 ^ total]
        for i in encoded:
            ans.append(ans[-1] ^ i)

        return ans
