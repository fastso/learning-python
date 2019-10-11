n = int(input())
a = list(map(int, input().split()))

start = min(a)
end = max(a)

ans = float('inf')
for i in range(start, end + 1):
    temp = 0
    for j in a:
        temp += (j - i) ** 2
    ans = min(ans, temp)
print(ans)
