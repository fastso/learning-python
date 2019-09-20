n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))

p.append(a)
p.append(b)

p_del = set(p)

if len(p) == len(p_del):
    print('YES')
else:
    print('NO')
