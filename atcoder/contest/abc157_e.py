n = int(input())
s = list(input())
q = int(input())

s_dict = dict()
for i in range(len(s)):
    if s[i] in s_dict:
        s_dict[s[i]] += 1
    else:
        s_dict[s[i]] = 1

for i in range(q):
    a, b, c = map(str, input().split())
    if a == '1':
        b = int(b) - 1
        # 文字挿入
        temp = s[b]
        if s_dict[temp] > 0:
            s_dict[temp] -= 1
        s[b] = c
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
    elif a == '2':
        b = int(b) - 1
        c = int(c) - 1
        # 文字種類カウント
        temp = s[b:c + 1]
        count = 0
        for k, v in s_dict.items():
            if v > 0:
                if k in temp:
                    count += 1
        print(count)
