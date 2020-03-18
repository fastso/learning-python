s = list(input())

ans = 0
for i in range(2 ** (len(s) - 1)):
    s_copy = s[:]
    for j in reversed(range(len(s))):
        if (i >> j) & 1:
            s_copy.insert(j + 1, '+')
    cut = ''.join(s_copy).split('+')

    for j in cut:
        ans += int(j)

print(ans)
