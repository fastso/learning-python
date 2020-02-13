from typing import List


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        l = list(s)
        ans = list()
        for i in range(len(l) - 1):
            if l[i + 1] == l[i] == '+':
                temp = l[:]
                temp[i + 1] = '-'
                temp[i] = '-'
                ans.append(''.join(temp))
        return ans
