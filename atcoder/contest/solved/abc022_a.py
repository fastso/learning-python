n, s, t = map(int, input().split())
w = 0
result = 0
for i in range(n):
    w += int(input())
    if s <= w <= t:
        result += 1
print(result)
