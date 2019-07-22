n = int(input())
a = [input() for i in range(n)]

for i in range(1, n):
    if a.count(a[i]) > 1:
        print('No')
        exit()
    if a[i-1][-1] != a[i][0]:
        print('No')
        exit()

print('Yes')
