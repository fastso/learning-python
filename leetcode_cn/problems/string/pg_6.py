class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        s_m = ['' for _ in range(numRows)]
        down = True
        x = 0
        y = 0
        s_m[0] = s[0]

        for i in range(1, len(s)):
            if down:
                y += 1
                s_m[y] += s[i]
                if y == numRows - 1:
                    down = False
            else:
                x += 1
                y -= 1
                s_m[y] += s[i]
                if y == 0:
                    down = True

        ans = ''
        for i in s_m:
            for j in i:
                if j:
                    ans += j

        return ans
