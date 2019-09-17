a, b = map(int, input().split())

ans = 0
c = 1
while c < b:
    c += a - 1
    ans += 1
print(ans)
