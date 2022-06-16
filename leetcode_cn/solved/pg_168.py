class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return 'A'
        ans = []
        while columnNumber > 0:
            ans.append(chr(ord('A') + (columnNumber - 1) % 26))
            columnNumber = (columnNumber - 1) // 26
        return ''.join(ans[::-1])
