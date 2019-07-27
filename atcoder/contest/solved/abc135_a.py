a, b = map(int, input().split())
print('IMPOSSIBLE' if abs(b - a) % 2 != 0 else (a + b) // 2)
