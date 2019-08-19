n = int(input())
a = [int(input()) for i in range(n)]
visited = [0]*n

ans = 0
pos = 0
while True:
    ans += 1
    if visited[pos] == 1:
        print(-1)
        exit()
    visited[pos] = 1
    pos = a[pos] - 1
    if pos == 1:
        print(ans)
        exit()
