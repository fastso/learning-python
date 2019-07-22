n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
diff = 100000
for i in range(n):
    if abs(t - h[i] * 0.006 - a) < diff:
        ans = i + 1
        diff = abs(t - h[i] * 0.006 - a)

print(ans)
