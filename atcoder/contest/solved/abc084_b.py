import re

a, b = map(str, input().split())
s = input()

pattern = r'^[0-9]{' + a + '}-[0-9]{' + b + '}$'
m = re.match(pattern, s)

if m:
    print('Yes')
else:
    print('No')
