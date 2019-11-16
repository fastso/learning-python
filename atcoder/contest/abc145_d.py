from collections import deque

x, y = map(int, input().split())

directions = [(1, 2), (2, 1)]

start = [0, 0]
end = [x, y]

queue = deque([start])

ans = 0
while queue:
    now = queue.popleft()
    if now[0] > end[0] or now[1] > end[1]:
        continue
    elif now[0] == end[0] or now[1] == end[1]:
        ans += 1
    else:
        for d in directions:
            queue.append([now[0] + d[0], now[1] + d[1]])
print(ans)
