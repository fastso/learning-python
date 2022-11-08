import sys
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_value = sys.maxsize
        for i in range(len(arr) - 1):
            diff = abs(arr[i+1] - arr[i])
            if diff > min_value:
                continue

            if diff < min_value:
                ans.clear()
                min_value = diff

            ans.append([arr[i], arr[i+1]])
        return ans

