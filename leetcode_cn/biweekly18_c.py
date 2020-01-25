from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0]*n for _ in range(m)]

        # 縦
        for k in range(m):
            i = k
            j = 0
            temp_list = list()
            while i < m and j < n:
                temp_list.append(mat[i][j])
                i += 1
                j += 1
            temp_list.sort()

            i = k
            j = 0
            for c in temp_list:
                ans[i][j] = c
                i += 1
                j += 1

        # 横
        for k in range(1, n):
            i = 0
            j = k
            temp_list = list()
            while i < m and j < n:
                temp_list.append(mat[i][j])
                i += 1
                j += 1
            temp_list.sort()

            i = 0
            j = k
            for c in temp_list:
                ans[i][j] = c
                i += 1
                j += 1

        return ans
