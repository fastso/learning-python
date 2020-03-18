"""
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d

4≤N≤30000のため、
素直に全探索をするとO(n^3)がかかり、間に合わない。
選び出した数値が3桁のため、000 - 999の数値が暗証番号になり得るかを調べると、
O(1000 * n)で間に合う。
"""

n = int(input())
s = list(input())

ans = 0
for i in range(1000):
    temp = [str(i // 100), str((i // 10) % 10), str(i % 10)]
    count = 0
    for j in range(n):
        if temp[count] == s[j]:
            count += 1
        if count == 3:
            ans += 1
            break
print(ans)
