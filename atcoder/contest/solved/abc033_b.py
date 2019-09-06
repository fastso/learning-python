n = int(input())
a = [list(map(str, input().split())) for i in range(n)]

a_sum = 0
for i in range(n):
    a_sum += int(a[i][1])

for i in range(n):
    if int(a[i][1]) > (a_sum / 2):
        print(a[i][0])
        exit()
print('atcoder')
