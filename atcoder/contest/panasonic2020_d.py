n = int(input())

a = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

ans = ['a'] * n
temp = ans[:]

print(''.join(ans))

# 最後 to 1 (変換区間決定)
for i in reversed(range(1, n)):
    temp = ans[:]
    for j in range(i, n):
        current = a[j - i]
        for k in range(j, n):
            temp[k] = current
            print(''.join(temp))