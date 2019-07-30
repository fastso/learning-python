n = int(input())
t = [list(map(int, input().split())) for i in range(n)]

t.sort(key=lambda x: (x[1], x[0]))

now = 0
for i in range(n):
    now += t[i][0]
    if now > t[i][1]:
        print('No')
        exit()
print('Yes')
