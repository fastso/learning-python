n, k = map(int, input().split())
s = list(input())

if s[0] == s[-1]:
    alphabet = s[0]
    if alphabet == 'L':
        alphabet = 'R'
    else:
        alphabet = 'L'
    for i in range(n):
        if s[i] != alphabet:
            s[i] = alphabet
        else:
            break
    for i in reversed(range(n)):
        if s[i] != alphabet:
            s[i] = alphabet
        else:
            break
else:
    alphabet = s[0]
    if alphabet == 'L':
        alphabet = 'R'
    else:
        alphabet = 'L'
    for i in range(n):
        if s[i] != alphabet:
            s[i] = alphabet
        else:
            break

for i in range(k - 1):
    alphabet = s[0]
    if alphabet == 'L':
        alphabet = 'R'
    else:
        alphabet = 'L'
    for i in range(n):
        if s[i] != alphabet:
            s[i] = alphabet
        else:
            break
    for i in reversed(range(n)):
        if s[i] != alphabet:
            s[i] = alphabet
        else:
            break

print(s)
ans = 0
for i in range(n):
    if s[i] == 'R':
        if i + 1 < n and s[i + 1] == 'R':
            ans += 1
    elif [i] == 'L':
        if i - 1 >= 0 and s[i - 1] == 'L':
            ans += 1
print(ans)
