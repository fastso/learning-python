class Solution:
    def countDigitOne(self, n: int) -> int:
        dp = [[[0] * 2 for i in range(2)] for j in range(32)]
        # dp[決定済み桁数][未満フラグ][1を含むフラグ]

        s = str(n)
        s_len = len(s)

        # 初期化
        dp[0][0][0] = 1
        dp[0][0][1] = 0
        dp[0][1][0] = 0
        dp[0][1][1] = 0

        for i in range(s_len):
            d = int(s[i])
            for j in range(2):
                for k in range(2):
                    if j:
                        temp = 9
                    else:
                        temp = d
                    for x in range(temp + 1):
                        dp[i + 1][j or (x < d)][k or x == 1] += dp[i][j][k]
                        if x == 1:
                            dp[i + 1][j or (x < d)][1] += 1

        return dp[s_len][0][1] + dp[s_len][1][1]
