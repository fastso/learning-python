from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = list()
        hash_table = {}
        for i in nums1:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for i in nums2:
            if i in hash_table:
                if hash_table[i] != 0:
                    ans.append(i)
                    hash_table[i] -= 1

        return ans
