from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows >= 1:
            ans.append([1])
        if numRows >= 2:
            ans.append([1, 1])

        for i in range(2, numRows):
            pre_floor = ans[i - 1]
            floor = [1]
            for j in range(1, len(pre_floor)):
                floor.append(pre_floor[j - 1] + pre_floor[j])
            floor.append(1)
            ans.append(floor)
        return ans
