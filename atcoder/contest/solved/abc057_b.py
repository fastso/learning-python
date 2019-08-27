n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
c = [list(map(int, input().split())) for i in range(m)]

for i in range(n):
    dist_min = float('inf')
    dist_min_pos = 0
    for j in range(m):
        dist = abs(a[i][0] - c[j][0]) + abs(a[i][1] - c[j][1])
        if dist < dist_min:
            dist_min = dist
            dist_min_pos = j + 1
    print(dist_min_pos)
