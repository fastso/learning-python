n, m = map(int, input().split())
a = [list(input()) for i in range(n)]
b = [list(input()) for i in range(m)]

for i in range(n - m + 1):
    for j in range(n - m + 1):
        ans = 0
        for k in range(m):
            if b[k] == a[i+k][j:j+m]:
                ans += 1
        if ans == m:
            print('Yes')
            exit()
print('No')
