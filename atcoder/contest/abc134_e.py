n = int(input())
l = [int(input()) for i in range(n)]

ans = [l[0]]
for i in range(1, len(l)):
    if l[i] <= ans[-1]:
        ans.append(l[i])
        continue
    for j in range(len(ans)):
        if l[i] > ans[j]:
            ans[j] = l[i]
            break
    list.sort(ans, reverse=True)

print(len(ans))
