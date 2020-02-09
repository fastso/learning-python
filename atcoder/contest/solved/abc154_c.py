n = int(input())
a = list(map(int, input().split()))

s = set(a)
if len(s) == n:
    print('YES')
else:
    print('NO')