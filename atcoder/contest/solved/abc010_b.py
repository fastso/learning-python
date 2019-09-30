n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    while (i - 2) % 3 == 0 or i % 2 == 0:
        i -= 1
        ans += 1
print(ans)
