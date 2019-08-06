"""
最長共通部分列(Longest Common Sub-sequence)

Input Sample:
axyb
abyxb

Output Sample:
axb

References:
https://qiita.com/drken/items/03c7db44ccd27820ea0d#f-%E5%95%8F%E9%A1%8C---lcs
"""

s1 = list(input())
s2 = list(input())

dp = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]

s1.insert(0, ' ')
s2.insert(0, ' ')

# 長さ計算
max_len = 0
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        max_len = max(max_len, dp[i][j])

# 復元
ans = []
i = len(s1) - 1
j = len(s2) - 1
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans.insert(0, s1[i])
        i -= 1
        j -= 1
print(''.join(ans))
