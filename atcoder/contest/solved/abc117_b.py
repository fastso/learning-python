n = int(input())
a = list(map(int, input().split()))

a.sort()
if a[-1] < sum(a[:n-1]):
    print('Yes')
else:
    print('No')
