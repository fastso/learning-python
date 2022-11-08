from collections import Counter
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = Counter()  # 出現回数
        freq = Counter()  # freq[x] : 出現回数がxの数の要素数
        ans = 0
        max_freq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            max_freq = max(max_freq, count[num])
            freq[count[num]] += 1
            if max_freq == 1 or freq[max_freq] * max_freq + freq[max_freq - 1] * (max_freq - 1) == i + 1 and freq[
                max_freq] == 1 or freq[max_freq] * max_freq + 1 == i + 1 and freq[1] == 1:
                ans = max(ans, i + 1)
        return ans
