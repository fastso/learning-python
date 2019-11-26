class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(n-1):
            ans = self.next_ans(ans)
        return ans

    def next_ans(self, s: str) -> str:
        count = 0
        ans = ''
        for i in range(len(s)):
            if i + 1 >= len(s) or s[i + 1] != s[i]:
                count += 1
                ans += str(count)
                ans += str(s[i])
                count = 0
            else:
                count += 1
        return ans
