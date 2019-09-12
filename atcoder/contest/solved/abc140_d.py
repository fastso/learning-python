n, k = map(int, input().split())
s = list(input())

s_c = []

left = 0
right = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        right = i + 1
    else:
        s_c.append(''.join(s[left:right + 1]))
        i += 1
        left = i
        right = i
s_c.append(''.join(s[left:right + 1]))

s_c_len = len(s_c)
cc = 'R'
if s_c_len > 1 and s_c[1][0] == 'R':
    cc = 'L'

for i in range(k):
    if (2 * i + 1) > s_c_len - 1:
        break
    s_c[2 * i + 1] = cc * len(s_c[2 * i + 1])

ans_s = ''.join(s_c)
ans = 0
for i in range(n):
    if ans_s[i] == 'R' and i != n - 1 and ans_s[i + 1] == 'R':
        ans += 1
    elif ans_s[i] == 'L' and i != 0 and ans_s[i - 1] == 'L':
        ans += 1
print(ans)
