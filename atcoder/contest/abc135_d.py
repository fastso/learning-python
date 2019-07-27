s = input()

mod = 1000000007

ans = 0
s_list = list(s.replace('?', '0'))
h_pos = []
for i in range(len(s)):
    if s[i] == '?':
        h_pos.append(i)

if int(''.join(s_list)) % 13 == 5:
    ans += 1

for i in range(1, 10):
    for j in h_pos:
        s_list[j] = str(i)
        if int(''.join(s_list)) % 13 == 5:
            ans += 1
print(ans)
