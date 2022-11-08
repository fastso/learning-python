from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s1, s2):
            p_s1 = p_s2 = 0
            while p_s1 < len(s1) and p_s2 < len(s2):
                if s1[p_s1] == s2[p_s2]:
                    p_s1 += 1
                p_s2 += 1
            return p_s1 == len(s1)

        ans = -1
        for i in range(len(strs)):
            for j in range(len(strs)):
                if i != j and is_subsequence(strs[i], strs[j]):
                    break
            else:
                ans = max(ans, len(strs[i]))
        return ans
