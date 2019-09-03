n = int(input())

ans = float('inf')
for i in range(1, n+1):
    w = n // i
    for j in range(1, w+1):
        diff1 = abs(j - i)
        diff2 = n - j * i
        ans = min(ans, diff1 + diff2)
print(ans)
