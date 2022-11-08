from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        m, n, ls = len(words), len(words[0]), len(s)
        words_count = Counter(words)
        for i in range(ls - n * m + 1):
            window = [s[j:j + n] for j in range(i, i + n * m, n)]
            window_count = Counter(window)
            for word in words_count:
                if words_count[word] != window_count[word]:
                    break
            else:
                ans.append(i)
        return ans
