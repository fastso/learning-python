a = list(map(int, input().split()))

l = list()
for i in range(len(a) - 2):
    for j in range(i + 1, len(a) - 1):
        for k in range(j + 1, len(a)):
            l.append(a[i] + a[j] + a[k])
l.sort()
print(l[-3])
