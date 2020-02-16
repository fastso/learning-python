n = int(input())
s = [input() for _ in range(n)]

s_dict = dict()
s_max = 0

for i in s:
    if i not in s_dict:
        s_dict[i] = 1
        s_max = max(s_max, s_dict[i])
    else:
        s_dict[i] += 1
        s_max = max(s_max, s_dict[i])

ans = list()
for k, v in s_dict.items():
    if v == s_max:
        ans.append(k)

ans.sort()
for i in ans:
    print(i)
