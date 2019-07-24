n = int(input())

if n < 105:
    print(0)
    exit()

ans = 0
for i in range(105, n + 1, 2):
    c = 0
    for j in range(3, n // 2):
        if i % j == 0:
            c += 1
    if c == 6:
        ans += 1

print(ans)
