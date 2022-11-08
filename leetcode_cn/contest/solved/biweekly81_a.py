class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        count_flag = True
        for c in s:
            if c == '|':
                if count_flag:
                    count_flag = False
                else:
                    count_flag = True
            if count_flag and c == '*':
                ans += 1
        return ans

