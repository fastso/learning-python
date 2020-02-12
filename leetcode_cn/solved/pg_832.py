from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = list()
        for i in range(len(A)):
            temp = list()
            for j in reversed(range(len(A[0]))):
                if A[i][j] == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            ans.append(temp)
        return ans
