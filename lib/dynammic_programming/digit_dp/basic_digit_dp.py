"""
桁DP基礎

N以下の整数を数える。
"""


def basic_digit_dp(s: str) -> int:
    dp = [[0] * 2 for i in range(32)]
    # dp[決定済み桁数][未満フラグ]

    s_len = len(s)

    '''
    初期化
    dp[0]は「上から-1桁目までで条件を満たす数の総数」、N=5432とすると-1桁目は5の左隣、つまり0です。
    0以下の整数は、0のみです。0は-1桁目に一致しているので、未満フラグ=0になります。
    そのため、dp[0][0] = 1の状態から始まります。
    '''
    dp[0][0] = 1
    dp[0][1] = 0

    for i in range(s_len):
        d = int(s[i])
        for j in range(2):
            if j:
                temp = 9
            else:
                temp = d
            for x in range(temp + 1):
                dp[i + 1][j or (x < d)] += dp[i][j]

    return dp[s_len][0] + dp[s_len][1]


s = input()
print(basic_digit_dp(s))
