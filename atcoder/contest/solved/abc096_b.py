a = list(map(int, input().split()))
k = int(input())

a.sort()
print(a[2] * (2 ** k) + a[1] + a[0])
