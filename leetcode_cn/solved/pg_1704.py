class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        return sum(c in vowels for c in s[:len(s) // 2]) == sum(c in vowels for c in s[len(s) // 2:])