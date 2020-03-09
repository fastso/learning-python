"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja

iは合計金額
dp[i]はi円を支払うためのコインの最小枚数
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    c = list(map(int, input().split()))

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i >= c[j]:
                dp[i] = min(dp[i - c[j]] + 1, dp[i])
    print(dp[n])
