n, m, x, y = map(int, input().split())
xa = list(map(int, input().split()))
ya = list(map(int, input().split()))

xa.sort()
ya.sort()

if xa[-1] < ya[0] and (x < xa[-1] + 1 <= y or x < ya[0] <= y):
    print('No War')
else:
    print('War')
