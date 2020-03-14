"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp

reference:
http://kutimoti.hatenablog.com/entry/2018/03/10/220819

Python TLE
"""
while True:
    n = int(input())
    if n == 0:
        break

    w = list(map(int, input().split()))

    dp = [[0] * n for _ in range(n)]

    # size : [2, n]
    for size in range(2, n + 1):
        # left : [0, n)
        for l in range(n):
            r = l + size - 1
            if r >= n:
                break
            # do something
            if dp[l + 1][r - 1] == size - 2 and abs(w[l] - w[r]) <= 1:
                dp[l][r] = size

            for mid in range(l, r):
                # Example :
                dp[l][r] = max(dp[l][r], dp[l][mid] + dp[mid + 1][r])

    print(dp[0][n - 1])
