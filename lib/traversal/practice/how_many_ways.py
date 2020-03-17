"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
"""

while True:
    n, x = map(int, input().split())
    if not n and not x:
        break

    ans = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    ans += 1
    print(ans)
