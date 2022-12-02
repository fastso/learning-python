class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        mod = 10 ** 9 + 7
        ans = 0
        dp = [[0] * n for i in range(n)]

