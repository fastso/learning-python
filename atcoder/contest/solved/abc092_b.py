n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]

ans = x
for i in range(n):
    for j in range(d):
        if j * a[i] + 1 <= d:
            ans += 1
        else:
            break
print(ans)
