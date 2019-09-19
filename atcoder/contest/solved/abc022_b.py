n = int(input())
s = {}

ans = 0
for i in range(n):
    a = int(input())
    if a in s:
        ans += 1
    else:
        s[a] = a
print(ans)
