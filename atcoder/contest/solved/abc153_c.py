n, k = map(int, input().split())
h = list(map(int, input().split()))

if k >= n:
    print(0)
    exit()
h.sort()
print(sum(h[:n - k]))
