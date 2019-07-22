x1, y1, x2, y2 = map(int, input().split())

a = x2 - x1
b = y2 - y1

print(str(x2 - b) + ' ' + str(y2 + a) + ' ' + str(x1 - b) + ' ' + str(y1 + a))
