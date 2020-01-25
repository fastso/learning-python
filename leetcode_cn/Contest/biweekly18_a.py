from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = list(set(arr))
        arr_sorted.sort()
        d = dict()
        for k, v in enumerate(arr_sorted):
            d[v] = k + 1

        ans = list()
        for i in arr:
            ans.append(d[i])

        return ans
