class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        """

        :param N:
        :return:
        """
        dp = [[[0] * 2 for i in range(2)] for j in range(10)]
        # dp[決定済み桁数][未満フラグ][重複数字を含むかフラグ]

        # 初期化
        dp[0][0][0] = 1

        s = str(N)
        s_len = len(s)
        current_s = list()

        for i in range(s_len):
            d = int(s[i])
            current_s.append(d)
            print(current_s)
            for j in range(2):
                for k in range(2):
                    if j:
                        temp = 9
                    else:
                        temp = d
                    for x in range(temp + 1):
                        dp[i + 1][j or (x < d)][k or (x in current_s)] += dp[i][j][k]

        return dp[s_len][0][1] + dp[s_len][1][1]
