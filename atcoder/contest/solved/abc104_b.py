s = input()

ans = True
if s[0] == 'A' and s[1].islower() and s[-1].islower() and s[2:len(s) - 1].count('C') == 1:
    for i in range(2, len(s) - 1):
        if s[i].isupper() and s[i] != 'C':
            ans = False
else:
    ans = False

print('AC' if ans else 'WA')
