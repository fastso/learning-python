from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = s.rfind(s[0])

        ans = list()
        i = 0
        j = 0
        while i < len(s):
            j = i
            end = max(end, s.rfind(s[j]))
            while j < end:
                end = max(end, s.rfind(s[j]))
                j += 1

            ans.append(j + 1 - i)
            i = j + 1

        return ans
