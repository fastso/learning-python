a, b = map(int, input().split())

ans = max(a+b, a-b)
ans = max(ans, a*b)

print(ans)
