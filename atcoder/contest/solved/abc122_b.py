s = input()

ans = 0
n = 0
for i in s:
    if i in 'ACGT':
        n += 1
        ans = max(ans, n)
    else:
        n = 0
print(ans)
