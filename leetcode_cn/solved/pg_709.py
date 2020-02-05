class Solution:
    def toLowerCase(self, s: str) -> str:
        l = list(s)
        for i in range(len(l)):
            o = ord(l[i])
            if 64 < o < 91:
                o += 32
                l[i] = chr(o)
        return ''.join(l)
