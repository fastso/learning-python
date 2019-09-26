n, x = map(int, input().split())
a = list(map(int, input().split()))

x = bin(x)[2:]

ans = 0
for i in range(1, len(x)+1):
    if x[-i] == '1':
        ans += a[i-1]
print(ans)
