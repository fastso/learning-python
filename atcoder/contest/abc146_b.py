n = int(input())
s = list(input())

a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in range(len(s)):
    for j in range(len(a)):
        if s[i] == a[j]:
            s[i] = a[(j + n) % 26]
            break
print(''.join(s))
