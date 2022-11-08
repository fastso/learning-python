from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = list()
        for i in range(len(nums1)):
            diff.append(abs(nums1[i] - nums2[i]))
        diff.sort()

        for i in range(len(diff)):
            if diff[i] >= k1:
                return diff[i] ** 2
