n = int(input())
a = [int(input()) for i in range(n)]

a.sort()
ans = sum(a)

if ans % 10 != 0:
    print(ans)
    exit()
for i in range(n):
    if a[i] % 10 != 0:
        print(ans - a[i])
        exit()
print(0)
