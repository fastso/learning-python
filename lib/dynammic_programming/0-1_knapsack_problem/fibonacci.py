"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja
"""

if __name__ == '__main__':
    n = int(input())
    ans = [1, 1, ]
    if n == 0 or n == 1:
        print(ans[n])
    else:
        for i in range(2, n + 1):
            ans.append(ans[i - 2] + ans[i - 1])
        print(ans[n])
