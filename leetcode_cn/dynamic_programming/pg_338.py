from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = list()
        ans.append(0)
        for i in range(1, num + 1):
            if i % 2 == 1:
                ans.append(ans[i - 1] + 1)
            else:
                ans.append(ans[i // 2])
        return ans
