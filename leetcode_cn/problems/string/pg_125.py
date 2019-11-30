class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = set(list('abcdefghijklmnopqrstuvwxyz0123456789'))
        left = 0
        right = len(s) - 1

        s = s.lower()
        while left < right:
            while s[left] not in check:
                left += 1
                if left > len(s) - 1:
                    return True
            while s[right] not in check:
                right -= 1
                if right < 0:
                    return True
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
