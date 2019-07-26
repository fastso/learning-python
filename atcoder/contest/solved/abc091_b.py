m = int(input())
a1 = [input() for i in range(m)]
n = int(input())
a2 = [input() for i in range(n)]

ans = 0
for i in a1:
    ans = max(ans, a1.count(i) - a2.count(i))
print(ans)
