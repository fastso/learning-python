class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        p = [0]
        for c in s:
            p.append(p[-1] + int(c))

        return min(p[i] + len(s) - i - (p[-1] - p[i]) for i in range(len(p)))
