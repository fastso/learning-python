n = int(input())
l = list(map(int, input().split()))

ans = 0
min_val = l[0]
for i in range(n):
    if min_val >= l[i]:
        ans += 1
        min_val = l[i]
print(ans)
