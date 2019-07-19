n, m = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in range(1, m+1):
    ans += 1
    for j in range(n):
        if i not in a[j][1:]:
            ans -= 1
            break
print(ans)
