"""
https://atcoder.jp/contests/atc001/tasks/dfs_a
"""
h, w = map(int, input().split())
maze = [list(input()) for y in range(h)]
reached = [[0] * w for y in range(h)]

for i in range(h):
    for j in range(w):
        if maze[i][j] == 's':
            s_y = i
            s_x = j
        elif maze[i][j] == 'g':
            g_y = i
            g_x = j

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
stack = [[s_y, s_x]]
reached[s_y][s_x] = 1

while stack:
    now = stack.pop()
    for d in directions:
        next_y = now[0] + d[0]
        next_x = now[1] + d[1]
        if 0 <= next_y < h and 0 < next_x < w:
            if maze[next_y][next_x] == '.' or maze[next_y][next_x] == 'g':
                if reached[next_y][next_x] == 0:
                    stack.append(now)
                    stack.append([next_y, next_x])
                    reached[next_y][next_x] = 1
                    break

print('Yes' if reached[g_y][g_x] == 1 else 'No')
