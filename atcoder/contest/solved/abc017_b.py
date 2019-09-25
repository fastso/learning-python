s = list(input())

for i in range(len(s)):
    if s[i] == 'c':
        if i + 1 < len(s) and s[i + 1] == 'h':
            continue
        else:
            print('NO')
            exit()
    elif s[i] == 'h':
        if i - 1 >= 0 and s[i - 1] == 'c':
            continue
        else:
            print('NO')
            exit()
    elif s[i] == 'o':
        continue
    elif s[i] == 'k':
        continue
    elif s[i] == 'u':
        continue
    else:
        print('NO')
        exit()
print('YES')
