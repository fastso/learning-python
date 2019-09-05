s = input()
t = int(input())

h = 0
x = 0
y = 0

for i in s:
    if i == 'L':
        x -= 1
    elif i == 'R':
        x += 1
    elif i == 'U':
        y += 1
    elif i == 'D':
        y -= 1
    else:
        h += 1

dis = abs(x) + abs(y)
if t == 1:
    print(dis + h)
else:
    if h >= dis:
        print(0 if (h - dis) % 2 == 0 else 1)
    else:
        print(dis - h)
