n, k, q = map(int, input().split())
k -= q

if k > 0:
    for i in range(n):
        print('Yes')
    exit()

a = [int(input()) for i in range(q)]
n_a = [k] * n

for i in range(q):
    n_a[a[i] - 1] += 1

ans = 0
for i in n_a:
    if i <= 0:
        print('No')
    else:
        print('Yes')
