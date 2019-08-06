h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]
reached = [[0] * w for j in range(h)]

for i in range(h):
    for j in range(w):
        if maze[i][j] == 's':
            s_i = i
            s_j = j
        elif maze[i][j] == 'g':
            g_i = i
            g_j = j

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
stack = [[s_i, s_j]]
reached[s_i][s_j] = 1

while stack:
    now = stack.pop()
    for d in directions:
        next_i = now[0] + d[0]
        next_j = now[1] + d[1]
    if 0 <= next_i < h and 0 < next_j < w:
        if maze[next_i][next_j] == '.' or maze[next_i][next_j] == 'g':
            if reached[next_i][next_j] == 0:
                stack.append(now)
                stack.append([next_i, next_j])
                reached[next_i][next_j] = 1

print('Yes' if reached[g_i][g_j] == 1 else 'No')
