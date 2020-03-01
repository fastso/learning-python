n, m = map(int, input().split())

ans = [-1] * n
for i in range(m):
    s, c = map(int, input().split())
    s = s - 1
    if ans[s] != -1 and ans[s] != c:
        print(-1)
        exit()
    if n != 1 and s == 0 and c == 0:
        print(-1)
        exit()
    ans[s] = c

for i in range(n):
    if ans[i] == -1:
        ans[i] = '0'
    else:
        ans[i] = str(ans[i])

if ans[0] == '0' and n != 1:
    ans[0] = '1'
print(''.join(ans))
