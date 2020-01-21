a, b = map(int, input().split())
if a > b:
    print(''.join([str(b)] * a))
else:
    print(''.join([str(a)] * b))
