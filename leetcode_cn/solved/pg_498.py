from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        m, n = len(mat), len(mat[0])
        ans = []
        for i in range(m + n - 1):
            if i % 2 == 1:
                for j in range(max(0, i - n + 1), min(m, i + 1)):
                    ans.append(mat[j][i - j])
            else:
                for j in range(max(0, i - m + 1), min(n, i + 1)):
                    ans.append(mat[i - j][j])
        return ans