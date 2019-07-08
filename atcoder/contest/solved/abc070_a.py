a = input()

new_str = ''.join(list(reversed(a)))
if new_str == a:
    print('Yes')
else:
    print('No')
