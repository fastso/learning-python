import bisect

# A:神社の数　B:寺の数　Q:問いの数
A, B, Q = map(int, input().split())
INF = 10 ** 18

# 神社配列
s = [-INF] + [int(input()) for i in range(A)] + [INF]
# 寺配列
t = [-INF] + [int(input()) for i in range(B)] + [INF]

for q in range(Q):
    x = int(input())
    b, d = bisect.bisect_right(s, x), bisect.bisect_right(t, x)
    ans = INF
    for S in [s[b - 1], s[b]]:
        for T in [t[d - 1], t[d]]:
            d1, d2 = abs(S - x) + abs(T - S), abs(T - x) + abs(S - T)
            ans = min(ans, d1, d2)
print(ans)
