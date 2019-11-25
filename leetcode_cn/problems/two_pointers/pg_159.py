class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n

        left = 0
        right = 0
        hash_map = {}
        max_len = 2

        while right < n:
            if len(hash_map) < 3:
                hash_map[s[right]] = right
                right += 1

            if len(hash_map) == 3:
                # delete the leftmost character
                del_idx = min(hash_map.values())
                del hash_map[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len
