class Solution:
    def countLetters(self, S: str) -> int:
        ans = 1
        temp = 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                temp += 1
            else:
                temp = 1
            ans += temp
        return ans
