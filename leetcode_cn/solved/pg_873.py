from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        d = {}
        for i in range(len(arr)):
            d[arr[i]] = i
        ans = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                k = 2
                while a + b in d:
                    a, b = b, a + b
                    k += 1
                ans = max(ans, k)
        return ans if ans > 2 else 0
