from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        ans = len(words)
        for word in words:
            if len(word) > len(s):
                continue
            idx = -1
            for c in word:
                c_pos = pos[c]
                nxt = bisect_right(c_pos, idx)
                if nxt == len(c_pos):
                    ans -= 1
                    break
                idx = c_pos[nxt]
        return ans


