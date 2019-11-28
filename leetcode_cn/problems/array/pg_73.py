from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix[0])
        y = len(matrix)

        x0_flag = False
        y0_flag = False

        for i in range(x):
            if matrix[0][i] == 0:
                x0_flag = True
                break

        for j in range(y):
            if matrix[j][0] == 0:
                y0_flag = True
                break

        for i in range(1, x):
            for j in range(1, y):
                if matrix[j][i] == 0:
                    matrix[j][0] = matrix[0][i] = 0

        for i in range(1, x):
            for j in range(1, y):
                if matrix[j][0] == 0 or matrix[0][i] == 0:
                    matrix[j][i] = 0

        if x0_flag:
            for i in range(x):
                matrix[0][i] = 0

        if y0_flag:
            for j in range(y):
                matrix[j][0] = 0
