n = int(input())
a = [list(input()) for i in range(n)]

for i in range(n):
    line = []
    for j in reversed(range(n)):
        line.append(a[j][i])
    print(''.join(line))
