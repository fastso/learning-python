n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

count = 0
while count < m:
    for i in range(n):
        while a[i] > a[i+1]:
            a[i] //= 2
            count += 1
        if a[0] > a

for i in range(m):
    a[-1] //= 2
    a.sort()
print(sum(a))

def div(a, i):
    for i in range(i):
        a[i] //= 2