a = input()
b = input()

a = ''.join(list(reversed(a)))

if a == b:
    print('YES')
else:
    print('NO')
