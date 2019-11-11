n = int(input())
a = list(map(int, input().split()))

ans = [0] * 8
over_3200 = 0

for i in range(n):
    if a[i] < 400:
        ans[0] = 1
    elif a[i] < 800:
        ans[1] = 1
    elif a[i] < 1200:
        ans[2] = 1
    elif a[i] < 1600:
        ans[3] = 1
    elif a[i] < 2000:
        ans[4] = 1
    elif a[i] < 2400:
        ans[5] = 1
    elif a[i] < 2800:
        ans[6] = 1
    elif a[i] < 3200:
        ans[7] = 1
    else:
        over_3200 += 1

print(max(sum(ans), 1), end=' ')
print(sum(ans) + over_3200)
