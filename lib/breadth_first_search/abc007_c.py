from collections import deque

r, c = map(int, input().split())
s_y, s_x = map(int, input().split())
g_y, g_x = map(int, input().split())
s_y -= 1
s_x -= 1
g_y -= 1
g_x -= 1

maze = [list(input()) for i in range(r)]
reached = [[0] * c for i in range(r)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

queue = deque([[s_y, s_x, 0]])
reached[s_y][s_x] = 1

while queue:
    now = queue.popleft()
    depth = now[2] + 1
    for d in directions:
        next_y = now[0] + d[0]
        next_x = now[1] + d[1]
        if 0 <= next_y < r and 0 < next_x < c:
            if maze[next_y][next_x] == '.':
                if reached[next_y][next_x] == 0:
                    queue.append([next_y, next_x, depth])
                    reached[next_y][next_x] = 1

                    if next_y == g_y and next_x == g_x:
                        print(depth)
                        exit()
