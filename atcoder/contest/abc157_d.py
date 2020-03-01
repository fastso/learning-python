n, m, k = map(int, input().split())

relation = [[0] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    relation[a][b] = 1
    relation[b][a] = 1

for i in range(k):
    c, d = map(int, input().split())
    relation[c][d] = -1
    relation[d][c] = -1

ans = [0] * n
for i in range(n - 1):
    for j in range(i+1, n):
        if relation[i][j] == 1 or relation[i][j] == -1:
            continue
        else:

