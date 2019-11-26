from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        if not strs:
            return ans
        if len(strs) == 1:
            return strs[0]
        len_min = float('inf')
        flag = False
        for i in strs:
            len_min = min(len(i), len_min)

        for i in range(len_min):
            temp = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != temp:
                    flag = True
                    break
                if strs[j][i] == temp and j == len(strs) - 1:
                    ans += temp
            if flag:
                break
        return ans
