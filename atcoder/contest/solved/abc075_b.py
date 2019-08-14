h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for y in range(h):
    for x in range(w):
        if s[y][x] != '.':
            continue
        p_sum = 0
        for z in direction:
            if 0 <= y + z[0] < h and 0 <= x + z[1] < w:
                if s[y + z[0]][x + z[1]] == '#':
                    p_sum += 1
        s[y][x] = p_sum

for y in range(h):
    for x in range(w):
        print(s[y][x], end='')
    print()
