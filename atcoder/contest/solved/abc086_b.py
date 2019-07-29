import math

a, b = map(str, input().split())
c = int(a + b)

if math.sqrt(c).is_integer():
    print('Yes')
else:
    print('No')
