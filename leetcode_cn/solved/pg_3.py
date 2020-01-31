class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        s_l = list(s)
        left = 0
        hashmap = {}
        ans = 0

        for right in range(s_len):
            if s_l[right] in hashmap:
                left = max(hashmap.get(s_l[right]), left)
            ans = max(ans, right - left + 1)
            hashmap[s_l[right]] = right + 1
        return ans
