class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        new_s = s[::-1]
        return s == new_s
