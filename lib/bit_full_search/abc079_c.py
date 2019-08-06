s = list(input())
n = len(s)
for i in range(2 ** (n - 1)):
    ans = int(s[0])
    for j in reversed(range(n - 1)):
        if (i >> j) & 1:
            ans += int(s[j + 1])
        else:
            ans -= int(s[j + 1])
    if ans == 7:
        for j in reversed(range(n - 1)):
            if (i >> j) & 1:
                s.insert(j + 1, '+')
            else:
                s.insert(j + 1, '-')
        print(''.join(s) + '=7')
        exit()
