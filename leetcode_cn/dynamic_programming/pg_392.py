class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        now = 0
        for i in t:
            if s[now] == i:
                now += 1
            if now == len(s):
                return True
        return False
