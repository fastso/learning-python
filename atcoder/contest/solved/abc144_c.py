import math

n = int(input())
x = int(math.sqrt(n)) + 1

ans = float('inf')
for i in range(1, x + 1):
    if n % i == 0:
        ans = min((i + n / i - 2), ans)
print(int(ans))
