a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    if str(i)[::-1] == str(i):
        ans += 1
print(ans)
