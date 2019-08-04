s = list(input())
ans = [1] * len(s)

for i in range(len(s)):
    if s[i] == 'R' and s[i + 1] == 'L':
        for j in reversed(range(i)):
            if s[j] != 'R':
                break
            if (i - j) % 2 == 1:
                ans[i] += ans[j]
                ans[j] = 0
            else:
                ans[i + 1] += ans[j]
                ans[j] = 0

        for k in range(i + 2, len(s)):
            if s[k] != 'L':
                break
            if (k - i) % 2 == 1:
                ans[i] += ans[k]
                ans[k] = 0
            else:
                ans[i + 1] += ans[k]
                ans[k] = 0

for i in range(len(s)):
    if s[i] == 'R' and s[i + 1] == 'L':
        temp = ans[i]
        ans[i] = ans[i + 1]
        ans[i + 1] = temp

print(*ans)
