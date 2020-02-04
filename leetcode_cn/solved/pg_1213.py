from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        n_2 = len(arr2)
        n_3 = len(arr3)

        ans = list()
        j = 0
        k = 0
        for i in arr1:
            while j < n_2:
                if arr2[j] < i:
                    j += 1
                else:
                    break
            while k < n_3:
                if arr3[k] < i:
                    k += 1
                else:
                    break
            if j == n_2 or k == n_3:
                break
            if i == arr2[j] == arr3[k]:
                ans.append(i)
        return ans
