class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        # dp[x][i][j] : 以字符x开始和结尾, 在s[i:j]子串中的回文数
        dp = [[[0] * n for _ in range(n)] for _ in range(4)]

        for i, c in enumerate(s):
            # 子串s[i]只有一个字符，回文数为1
            dp[ord(c) - ord('a')][i][i] = 1

        for sz in range(2, n + 1):
            # 子串长度为sz
            for j in range(sz - 1, n):
                # 子串的结尾为s[j]
                # 子串的开头为s[j - sz + 1]
                i = j - sz + 1
                for k, c in enumerate("abcd"):
                    if s[i] == c and s[j] == c:
                        # 子串的开头和结尾都为c，所以子串的回文数为2+dp[k][i+1][j-1] (2: 加上了cc和c子串c 两个回文)
                        dp[k][i][j] = (2 + sum(d[i + 1][j - 1] for d in dp)) % mod
                    elif s[i] == c:
                        # 子串的开头为c，结尾不为c，所以等价于dp[k][i][j-1]
                        dp[k][i][j] = dp[k][i][j - 1]
                    elif s[j] == c:
                        # 子串的结尾为c，开头不为c，所以等价于dp[k][i+1][j]
                        dp[k][i][j] = dp[k][i + 1][j]
                    else:
                        # 子串的开头和结尾都不为c，所以等价于dp[k][i+1][j-1]
                        dp[k][i][j] = dp[k][i + 1][j - 1]
        return sum(d[0][n - 1] for d in dp) % mod
