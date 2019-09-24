s = list(input())

ans = []
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        ans.append(s[i] + str(count))
        count = 1
print(''.join(ans) + s[-1] + str(count))
