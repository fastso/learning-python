n = int(input())
a = input()

if n % 2 != 0:
    print('No')
    exit()

n_2 = n // 2
if a[:n_2] == a[n_2:]:
    print('Yes')
else:
    print('No')
