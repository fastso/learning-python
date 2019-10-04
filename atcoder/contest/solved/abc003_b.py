s = list(input())
t = list(input())

a = list('atcoder')

for i in range(len(s)):
    if s[i] == t[i]:
        continue
    elif s[i] == '@':
        if t[i] in a:
            continue
        else:
            print('You will lose')
            exit()
    elif t[i] == '@':
        if s[i] in a:
            continue
        else:
            print('You will lose')
            exit()
    else:
        print('You will lose')
        exit()
print('You can win')
