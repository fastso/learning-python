class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ans = 0
        pre = 0
        for c in word:
            ans += abs(keyboard.index(c) - pre)
            pre = keyboard.index(c)
        return ans
