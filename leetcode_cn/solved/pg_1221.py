class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        ans = 0

        for c in s:
            if c == 'R':
                r += 1
            if c == 'L':
                l += 1

            if r == l:
                ans += 1
                r = 0
                l = 0
        return ans
