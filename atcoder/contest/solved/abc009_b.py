n = int(input())
a = [int(input()) for i in range(n)]

a.sort(reverse=True)

for i in range(1, n):
    if a[i] != a[0]:
        print(a[i])
        break
