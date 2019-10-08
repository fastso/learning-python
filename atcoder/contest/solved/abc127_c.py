n, m = map(int, input().split())

left = []
right = []
for i in range(m):
    a, b = map(int, input().split())
    left.append(a)
    right.append(b)
print(min(right) - max(left) + 1)
