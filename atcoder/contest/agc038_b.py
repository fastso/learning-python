n, k = map(int, input().split())
p = list(map(int, input().split()))

ans = 0
same_flag = True

for i in range(n - k + 1):
    same_len = 0
    temp = p[i:i + k]
    for j in range(i, i + k - 1):
        if p[j] < p[j + 1]:
            same_len += 1
            continue
        else:
            ans += 1
            break
    if same_flag and same_len == k - 1:
        ans += 1
        same_flag = False
    if same_len < k - 1:
        if i + k < n and p[i] == min(temp) and p[i + k] > max(temp):
            ans -= 1
            continue
print(ans)
