from collections import Counter
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = Counter(p % 2 for p in position)
        return min(cnt[0], cnt[1])
