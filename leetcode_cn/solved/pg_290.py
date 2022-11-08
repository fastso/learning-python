class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        d = {}
        for i, c in enumerate(pattern):
            if c in d:
                if d[c] != words[i]:
                    return False
            else:
                if words[i] in d.values():
                    return False
                d[c] = words[i]
        return True