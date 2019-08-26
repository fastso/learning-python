a = list(input())
b = list(input())

ans = []
for i in range(len(a)):
    ans.append(a[i])
    if i < len(b):
        ans.append(b[i])
print(''.join(ans))
